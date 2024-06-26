from nisync.devices.pxie6674t import (
    pfi_terminals,
    pfi_lvds_terminals,
    pxi_trig_terminals,
    pxi_dstarb_peripheral_terminal,
    pxi_dstarc_peripheral_terminal,
    global_software_trigger_terminal,
    sync_clock_terminals,
    ground_terminal,
)  # noqa: H301


model_code = 0x7406


number_of_logic_blocks = 8

logic_block_terminals_supported = ["LogicBlock%d" % i for i in range(number_of_logic_blocks)]

pxi_star_peripheral_terminal = ["PXI_Star"]

trigger_terminal_source_list = (
    pfi_terminals
    + pfi_lvds_terminals
    + pxi_star_peripheral_terminal
    + pxi_trig_terminals
    + pxi_dstarb_peripheral_terminal
    + global_software_trigger_terminal
    + sync_clock_terminals
    + ground_terminal
)

trigger_terminal_destination_list = (
    pfi_terminals
    + pfi_lvds_terminals
    + pxi_star_peripheral_terminal
    + pxi_trig_terminals
    + pxi_dstarc_peripheral_terminal
)

hardware_revisions = ["D", "E", "G", "H"]
temperature_supported = False
calibration_supported = False
