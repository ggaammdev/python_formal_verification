# Autonomous Formal Verification Workspace (Python)

This project bridges Python software logic with formal verification, enabling fully autonomous extraction, synthesis, and verification of Python state machines using the NuSMV model checker.

## Overview
Traditional formal verification requires engineers to manually translate software models into specialized specification languages (like SMV) and manually map counterexamples back to the code. This workspace automates that pipeline:
1. **Extraction**: A Python AST extractor parses your Python codebase and pulls out deterministic state transition logic.
2. **Synthesis**: The logic is autonomously synthesized into an equivalent `MODULE main` in native SMV syntax.
3. **Execution**: The NuSMV engine formally verifies your safety constraints (e.g. `CTLSPEC AG !(state = HW_ERROR)`).
4. **Analysis**: NuSMV trace outputs are mapped back to your original Python lines to catch edge-case bugs and race conditions.

## Project Structure
- `extractor/state_extractor.py`: Parses target Python files and outputs transitions as JSON.
- `examples/fpga_query_system/`: Sample Python application containing an `accelerator` and a `host_controller`.
- `smv_verification_agent.prompt.md`: The system prompt to run an AI agent through the fully autonomous execution loop.
- `output/`: Generated intermediate JSON and SMV models.

## Usage

Because this is an autonomous workspace, the primary usage is to execute the pipeline via an AI Agent:

1. **Provide the Prompt:** Supply the `smv_verification_agent.prompt.md` file to an autonomous AI agent (like ChatGPT, Claude, or a custom IDE agent) as its system prompt or initial context.
2. **Autonomous Execution:** The agent will autonomously read the codebase, run the `extractor/state_extractor.py`, synthesize the `output/generated_model.smv`, execute NuSMV, and propose patches for any counterexamples it finds.

*(Alternatively, you can manually run the extractor script and NuSMV commands yourself following the steps outlined in the agent prompt.)*

For detailed setup and installation instructions, please refer to [INSTALL.md](INSTALL.md).
