from nisync.devices.pxi6682 import pfi_terminals, pxi_trig_terminals  # noqa: H301,F401

model_code = 0x75E5

pxi_star_terminals = ["PXI_Star%d" % i for i in range(13)]
clock_terminals = ["PXI_Clk10", "PXI_Clk10_In", "ClkIn", "ClkOut", "Oscillator"]
ground_terminal = ["Ground"]

trigger_terminal_source_list = pfi_terminals + pxi_star_terminals + pxi_trig_terminals

trigger_terminal_destination_list = pfi_terminals + pxi_star_terminals + pxi_trig_terminals

hardware_revisions = ["D", "E", "G"]
temperature_supported = True
calibration_supported = True
