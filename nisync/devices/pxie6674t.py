model_code = 0x7405

number_of_logic_blocks = 8
logic_block_terminals_supported = ["LogicBlock%d" % i for i in range(number_of_logic_blocks)]

pfi_terminals = ["PFI%d" % i for i in range(6)]
pfi_lvds_terminals = ["PFI_LVDS%d" % i for i in range(3)]
pxi_star_terminals = ["PXI_Star%d" % i for i in range(17)]
pxi_trig_terminals = ["PXI_Trig%d" % i for i in range(8)]
pxi_dstara_peripheral_terminal = ["PXIe_DStarA"]
pxi_dstara_terminals = ["PXIe_DStarA%d" % i for i in range(17)]
pxi_dstarb_peripheral_terminal = ["PXIe_DStarB"]
pxi_dstarb_terminals = ["PXIe_DStarB%d" % i for i in range(17)]
pxi_dstarc_peripheral_terminal = ["PXIe_DStarC"]
pxi_dstarc_terminals = ["PXIe_DStarC%d" % i for i in range(17)]
global_software_trigger_terminal = ["GlobalSoftwareTrigger"]
sync_clock_terminals = ["SyncClkFullSpeed", "SyncClkDivided1", "SyncClkDivided2"]
ground_terminal = ["Ground"]
clock_terminals = [
    "PXI_Clk10",
    "PXI_Clk10_In",
    "ClkIn",
    "ClkOut",
    "Oscillator",
    "DDS",
    "PXIe_Clk100",
]

trigger_terminal_source_list = (
    pfi_terminals
    + pfi_lvds_terminals
    + pxi_star_terminals
    + pxi_trig_terminals
    + pxi_dstara_peripheral_terminal
    + pxi_dstarb_peripheral_terminal
    + pxi_dstarc_terminals
    + global_software_trigger_terminal
    + logic_block_terminals_supported
    + sync_clock_terminals
    + ground_terminal
)

trigger_terminal_destination_list = (
    pfi_terminals
    + pfi_lvds_terminals
    + pxi_star_terminals
    + pxi_trig_terminals
    + pxi_dstara_terminals
    + pxi_dstarb_terminals
    + pxi_dstarc_peripheral_terminal
)

# The PXIe-6674T timestamp FIFO is 0x400 or 1024 elements large.
timestamp_fifo_size = 0x400

hardware_revisions = ["C", "D", "E", "G", "H", "I"]
temperature_supported = True
calibration_supported = True
