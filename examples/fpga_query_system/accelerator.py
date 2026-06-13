from enum import Enum

class AcceleratorState(Enum):
    IDLE = 0
    PROCESSING = 1
    HW_ERROR = 2

class FpgaAccelerator:
    def __init__(self):
        self.state = AcceleratorState.IDLE
        self.data_ready = False

    def dispatch_query(self, valid_payload: bool):
        if self.state == AcceleratorState.IDLE:
            if valid_payload:
                self.state = AcceleratorState.PROCESSING
                self.data_ready = True
            else:
                self.state = AcceleratorState.HW_ERROR
                self.data_ready = False

    def reset(self):
        self.state = AcceleratorState.IDLE
        self.data_ready = False