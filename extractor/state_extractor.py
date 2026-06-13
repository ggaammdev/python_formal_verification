import ast
import sys
import json
import os

class StateTransitionVisitor(ast.NodeVisitor):
    def __init__(self):
        self.transitions = []
        self.condition_stack = []

    def visit_If(self, node):
        test_expr = ast.unparse(node.test)
        
        # Visit the main body with the condition pushed
        self.condition_stack.append(test_expr)
        for stmt in node.body:
            self.visit(stmt)
        self.condition_stack.pop()
        
        # Visit the else body with the negated condition pushed
        if node.orelse:
            self.condition_stack.append(f"not ({test_expr})")
            for stmt in node.orelse:
                self.visit(stmt)
            self.condition_stack.pop()

    def visit_Assign(self, node):
        # Look for assignments, specifically targeting class instance variables (self.something)
        for target in node.targets:
            if isinstance(target, ast.Attribute):
                lhs = ast.unparse(target)
                rhs = ast.unparse(node.value)
                self.transitions.append({
                    "transition_type": "assignment",
                    "variable": lhs,
                    "next_value": rhs,
                    "line": node.lineno,
                    "conditions": list(self.condition_stack)
                })
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        if isinstance(node.target, ast.Attribute):
            lhs = ast.unparse(node.target)
            rhs = ast.unparse(node.value)
            op = type(node.op).__name__
            self.transitions.append({
                "transition_type": "augmented_assignment",
                "variable": lhs,
                "operator": op,
                "value": rhs,
                "line": node.lineno,
                "conditions": list(self.condition_stack)
            })
        self.generic_visit(node)

    def visit_Call(self, node):
        func_name = ast.unparse(node.func)
        args = [ast.unparse(arg) for arg in node.args]
        self.transitions.append({
            "transition_type": "function_call",
            "function": func_name,
            "args": args,
            "line": node.lineno,
            "conditions": list(self.condition_stack)
        })
        self.generic_visit(node)

    def visit_Return(self, node):
        value = ast.unparse(node.value) if node.value else None
        self.transitions.append({
            "transition_type": "return_statement",
            "value": value,
            "line": node.lineno,
            "conditions": list(self.condition_stack)
        })
        self.generic_visit(node)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python state_extractor.py <file1.py> <file2.py> ...")
        sys.exit(1)

    files = sys.argv[1:]
    all_transitions = []

    for file_path in files:
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                tree = ast.parse(f.read(), filename=file_path)
                visitor = StateTransitionVisitor()
                visitor.visit(tree)
                # Append file context to each transition
                for transition in visitor.transitions:
                    transition["file"] = os.path.basename(file_path)
                all_transitions.extend(visitor.transitions)

    # Output as structured JSON for the AI to ingest
    print(json.dumps(all_transitions, indent=2))