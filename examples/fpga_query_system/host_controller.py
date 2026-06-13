from accelerator import FpgaAccelerator

class HostController:
    def __init__(self, accelerator: FpgaAccelerator):
        self.fpga = accelerator
        self.system_active = False

    def execute_cycle(self, incoming_query_valid: bool):
        self.system_active = True
        self.fpga.dispatch_query(incoming_query_valid)
        # SMV Specification to check: AG !(fpga.state = HW_ERROR)
        
    def shutdown(self):
        self.fpga.reset()
        self.system_active = False
