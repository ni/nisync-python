from nisync.devices.pxi6683 import calibration_supported  # noqa: H301,F401
from nisync.devices.pxi6682 import pfi_terminals, pxi_trig_terminals  # noqa: H301,F401
from nisync.devices.pxi6683 import temperature_supported, hardware_revisions  # noqa: H301,F401

model_code = 0x75E6

clock_terminals = ["PXI_Clk10", "ClkOut", "Oscillator"]
ground_terminal = ["Ground"]

trigger_terminal_source_list = pfi_terminals + pxi_trig_terminals

trigger_terminal_destination_list = pfi_terminals + pxi_trig_terminals
