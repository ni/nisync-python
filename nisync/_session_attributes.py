# This file was generated

from nisync import _attributes


class SessionAttributes(object):
    """SessionAttributes class encapsulates specific attributes related to a session."""

    interface_number = _attributes.AttributeViInt32(1150000)
    serial_number = _attributes.AttributeViInt32(1150001)
    pfi0_threshold = _attributes.AttributeViReal64(1150100)
    pfi1_threshold = _attributes.AttributeViReal64(1150101)
    pfi2_threshold = _attributes.AttributeViReal64(1150102)
    pfi3_threshold = _attributes.AttributeViReal64(1150103)
    pfi4_threshold = _attributes.AttributeViReal64(1150104)
    pfi5_threshold = _attributes.AttributeViReal64(1150105)
    oscillator_voltage = _attributes.AttributeViReal64(1150106)
    clk10_phase_adjust = _attributes.AttributeViReal64(1150107)
    dds_vcxo_voltage = _attributes.AttributeViReal64(1150108)
    dds_phase_adjust = _attributes.AttributeViReal64(1150109)
    pfi0_1kohm_enable = _attributes.AttributeViBoolean(1150110)
    pfi1_1kohm_enable = _attributes.AttributeViBoolean(1150111)
    pfi2_1kohm_enable = _attributes.AttributeViBoolean(1150112)
    pfi3_1kohm_enable = _attributes.AttributeViBoolean(1150113)
    pfi4_1kohm_enable = _attributes.AttributeViBoolean(1150114)
    pfi5_1kohm_enable = _attributes.AttributeViBoolean(1150115)
    pfi0_10kohm_enable = _attributes.AttributeViBoolean(1150116)
    pfi1_10kohm_enable = _attributes.AttributeViBoolean(1150117)
    pfi2_10kohm_enable = _attributes.AttributeViBoolean(1150118)
    pfi3_10kohm_enable = _attributes.AttributeViBoolean(1150119)
    pfi4_10kohm_enable = _attributes.AttributeViBoolean(1150120)
    pfi5_10kohm_enable = _attributes.AttributeViBoolean(1150121)
    front_sync_clk_src = _attributes.AttributeViString(1150200)
    rear_sync_clk_src = _attributes.AttributeViString(1150201)
    sync_clk_div1 = _attributes.AttributeViInt32(1150202)
    sync_clk_div2 = _attributes.AttributeViInt32(1150203)
    sync_clk_rst_pxitrig_num = _attributes.AttributeViString(1150204)
    sync_clk_pfi0_freq = _attributes.AttributeViReal64(1150205)
    sync_clk_rst_dds_cntr_on_pxitrig = _attributes.AttributeViBoolean(1150206)
    sync_clk_rst_pfi0_cntr_on_pxitrig = _attributes.AttributeViBoolean(1150207)
    sync_clk_rst_clk10_cntr_on_pxitrig = _attributes.AttributeViBoolean(1150208)
    terminal_state_pxistar = _attributes.AttributeViInt32(1150300)
    terminal_state_pxitrig = _attributes.AttributeViInt32(1150301)
    terminal_state_pfi = _attributes.AttributeViInt32(1150302)
    terminal_state_pxiedstarc = _attributes.AttributeViInt32(1150303)
    terminal_state_pfilvds = _attributes.AttributeViInt32(1150304)
    terminal_state_pxiedstarcperipheral = _attributes.AttributeViBoolean(1150305)
    terminal_state_pxiedstarbperipheral = _attributes.AttributeViBoolean(1150306)
    terminal_state_pxistarperipheral = _attributes.AttributeViBoolean(1150307)
    dds_frequency = _attributes.AttributeViReal64(1150400)
    dds_update_source = _attributes.AttributeViString(1150401)
    dds_initial_delay = _attributes.AttributeViReal64(1150402)
    clkin_pll_freq = _attributes.AttributeViReal64(1150500)
    clkin_use_pll = _attributes.AttributeViBoolean(1150501)
    clkin_pll_locked = _attributes.AttributeViBoolean(1150502)
    clkout_gain_enable = _attributes.AttributeViBoolean(1150503)
    pxiclk10_present = _attributes.AttributeViBoolean(1150504)
    clkin_attenuation_disable = _attributes.AttributeViBoolean(1150505)
    user_led_state = _attributes.AttributeViBoolean(1150600)
    ieee_1588_ip_address = _attributes.AttributeViString(1150700)
    ieee_1588_port_state = _attributes.AttributeViInt32(1150712)
    ieee_1588_steps_to_grandmaster = _attributes.AttributeViInt32(1150716)
    timestamp_buffer_size = _attributes.AttributeViInt32(1150718)
    available_timestamps = _attributes.AttributeViInt32(1150719)
    clock_resolution = _attributes.AttributeViInt32(1150720)
    ieee_1588_clock_id = _attributes.AttributeViString(1150729)
    ieee_1588_clock_class = _attributes.AttributeViInt32(1150730)
    ieee_1588_clock_accuracy = _attributes.AttributeViInt32(1150731)
    ieee_1588_priority1 = _attributes.AttributeViInt32(1150732)
    ieee_1588_priority2 = _attributes.AttributeViInt32(1150733)
    ieee_1588_grandmaster_clock_id = _attributes.AttributeViString(1150734)
    ieee_1588_grandmaster_clock_class = _attributes.AttributeViInt32(1150735)
    ieee_1588_grandmaster_clock_accuracy = _attributes.AttributeViInt32(1150736)
    ieee_1588_grandmaster_priority1 = _attributes.AttributeViInt32(1150737)
    ieee_1588_grandmaster_priority2 = _attributes.AttributeViInt32(1150738)
    ieee_1588_log_sync_interval = _attributes.AttributeViInt32(1150739)
    ieee_1588_mean_path_delay = _attributes.AttributeViReal64(1150740)
    ieee_1588_grandmaster_ip_address = _attributes.AttributeViString(1150741)
    ieee_1588_bmca_mode = _attributes.AttributeViInt32(1150742)
    ieee_1588_interface_name = _attributes.AttributeViString(1150743)
    ieee_1588_offset_scaled_log_variance = _attributes.AttributeViInt32(1150752)
    ieee_1588_leap59 = _attributes.AttributeViBoolean(1150763)
    ieee_1588_leap61 = _attributes.AttributeViBoolean(1150764)
    ieee_1588_time_traceable = _attributes.AttributeViBoolean(1150765)
    ieee_1588_frequency_traceable = _attributes.AttributeViBoolean(1150766)
    ieee_1588_time_source = _attributes.AttributeViInt32(1150768)
    time_reference_present = _attributes.AttributeViBoolean(1150800)
    time_reference_offset = _attributes.AttributeViReal64(1150802)
    time_reference_correction = _attributes.AttributeViReal64(1150804)
    time_reference_utc_offset = _attributes.AttributeViInt32(1150805)
    time_reference_utc_offset_valid = _attributes.AttributeViBoolean(1150806)
    time_reference_last_sync_id = _attributes.AttributeViInt32(1150807)
    time_reference_offset_ns = _attributes.AttributeViReal64(1150808)
    time_reference_selected_type = _attributes.AttributeViString(1150809)
    time_reference_type = _attributes.AttributeViString(1150810)
    time_reference_selected_name = _attributes.AttributeViString(1150811)
    time_reference_enabled = _attributes.AttributeViBoolean(1150812)
    time_reference_is_selected = _attributes.AttributeViBoolean(1150813)
    gps_antenna_connected = _attributes.AttributeViBoolean(1150900)
    gps_recalculate_position = _attributes.AttributeViBoolean(1150901)
    gps_satellites_available = _attributes.AttributeViInt32(1150902)
    gps_self_survey = _attributes.AttributeViInt32(1150903)
    gps_mobile_mode = _attributes.AttributeViBoolean(1150904)
    gps_status = _attributes.AttributeViInt32(1150905)
    ieee_8021as_port_state = _attributes.AttributeViInt32(1151100)
    ieee_8021as_clock_id = _attributes.AttributeViString(1151101)
    ieee_8021as_clock_class = _attributes.AttributeViInt32(1151102)
    ieee_8021as_clock_accuracy = _attributes.AttributeViInt32(1151103)
    ieee_8021as_priority1 = _attributes.AttributeViInt32(1151104)
    ieee_8021as_priority2 = _attributes.AttributeViInt32(1151105)
    ieee_8021as_grandmaster_clock_id = _attributes.AttributeViString(1151106)
    ieee_8021as_grandmaster_clock_class = _attributes.AttributeViInt32(1151107)
    ieee_8021as_grandmaster_clock_accuracy = _attributes.AttributeViInt32(1151108)
    ieee_8021as_grandmaster_priority1 = _attributes.AttributeViInt32(1151109)
    ieee_8021as_grandmaster_priority2 = _attributes.AttributeViInt32(1151110)
    ieee_8021as_log_sync_interval = _attributes.AttributeViInt32(1151111)
    ieee_8021as_log_announce_interval = _attributes.AttributeViInt32(1151112)
    ieee_8021as_interface_name = _attributes.AttributeViString(1151113)
    ieee_8021as_neighbor_prop_delay_thresh = _attributes.AttributeViInt32(1151114)
    ieee_8021as_as_capable = _attributes.AttributeViBoolean(1151115)
