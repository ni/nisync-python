# This file was generated

import ctypes
from datetime import timezone
from decimal import Decimal
from hightime import datetime
from hightime import timedelta

from nisync import _attributes
from nisync import _library_singleton
from nisync import _visatype
from nisync import enums
from nisync import errors


# we use TAI time in the driver and we want to keep
# this driver api free of leap seconds,
# so we don't use a timezone here
tai_epoch_no_tz = datetime(year=1970, month=1, day=1)


def _tai_timestamp_to_tai_time(tai_timestamp):
    seconds, microseconds = map(
        Decimal, divmod(Decimal(tai_timestamp) * Decimal(1e6), Decimal(1e6))
    )
    # no timezone, so simply add the seconds
    return tai_epoch_no_tz + timedelta(seconds=seconds, microseconds=microseconds)


def _tai_time_to_tai_timestamp(tai_time):
    # tai_time is a timezone-naive datetime in the TAI timescale
    # simply subtract the times
    diff = tai_time - tai_epoch_no_tz
    tai_timestamp = Decimal(diff.days * 24 * 60 * 60)
    tai_timestamp += Decimal(diff.seconds)
    tai_timestamp += Decimal(diff.microseconds) / Decimal(1e6)
    if hasattr(diff, "femtoseconds"):
        tai_timestamp += Decimal(diff.femtoseconds) / Decimal(1e15)
    return tai_timestamp


def _tai_time_parts_to_date_time(seconds, nanoseconds, frac_nanoseconds):
    # ignore frac_nanoseconds, not used
    microseconds = Decimal(nanoseconds) / Decimal(1e3)
    # no timezone, so simply add the seconds
    return tai_epoch_no_tz + timedelta(seconds=seconds, microseconds=microseconds)


def _date_time_to_tai_time_parts(date_time=None):
    if date_time is None:
        return 0, 0, 0
    tai_timestamp = Decimal(_tai_time_to_tai_timestamp(date_time))
    seconds, nanoseconds = map(Decimal, divmod(tai_timestamp * Decimal(1e9), Decimal(1e9)))
    frac_nanoseconds = 0
    return int(seconds), int(nanoseconds), int(frac_nanoseconds)


def _create_string_buffer(ascii_string):
    return ctypes.create_string_buffer(bytes(ascii_string.encode("ascii")))


class _SessionBase(object):
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

    def __init__(self, vi, library, active_item=None):
        self._vi = vi
        self._library = library
        self._active_item = active_item
        self._active_session_cache = {}

    def __call__(self, active_item):
        assert self._active_item is None
        if active_item in self._active_session_cache:
            return self._active_session_cache[active_item]
        self._active_session_cache[active_item] = self._get_active_session(active_item)
        return self._active_session_cache[active_item]

    def _get_active_session(self, active_item):

        class ActiveItemSession(_SessionBase):
            pass

        session = ActiveItemSession(self._vi, self._library, active_item)
        tr_name = active_item
        if tr_name.startswith("IEEE 1588") or tr_name.startswith("1588"):
            return IEEE1588TimeReference(session)
        elif tr_name.startswith("IEEE 802.1AS"):
            return IEEE8021ASTimeReference(session)
        elif tr_name.startswith("GPS"):
            return GPSTimeReference(session)
        elif tr_name.startswith("IRIG"):
            return IRIGBTimeReference(session)
        elif tr_name.startswith("EtherCAT"):
            return EtherCATTimeReference(session)
        elif tr_name.startswith("PPS"):
            return PPSTimeReference(session)
        else:
            return session

    def _get_error_description(self, code):
        vi_ctype = _visatype.ViSession(self._vi)
        code_ctype = _visatype.ViInt32(code)
        message_ctype = ctypes.create_string_buffer(256)
        error_code = self._library.niSync_error_message(vi_ctype, code_ctype, message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return str(message_ctype.value.decode())

    def _get_attribute_vi_int32(self, attribute):
        vi_ctype = _visatype.ViSession(self._vi)
        active_item_ctype = _create_string_buffer(self._active_item or "")
        attribute_ctype = _visatype.ViAttr(attribute)
        value_ctype = _visatype.ViInt32()
        error_code = self._library.niSync_GetAttributeViInt32(
            vi_ctype, active_item_ctype, attribute_ctype, ctypes.pointer(value_ctype)
        )
        errors.handle_error(self, error_code)
        return int(value_ctype.value)

    def _set_attribute_vi_int32(self, attribute, value):
        vi_ctype = _visatype.ViSession(self._vi)
        active_item_ctype = _create_string_buffer(self._active_item or "")
        attribute_ctype = _visatype.ViAttr(attribute)
        value_ctype = _visatype.ViInt32(value)
        error_code = self._library.niSync_SetAttributeViInt32(
            vi_ctype, active_item_ctype, attribute_ctype, value_ctype
        )
        errors.handle_error(self, error_code)

    def _get_attribute_vi_real64(self, attribute):
        vi_ctype = _visatype.ViSession(self._vi)
        active_item_ctype = _create_string_buffer(self._active_item or "")
        attribute_ctype = _visatype.ViAttr(attribute)
        value_ctype = _visatype.ViReal64()
        error_code = self._library.niSync_GetAttributeViReal64(
            vi_ctype, active_item_ctype, attribute_ctype, ctypes.pointer(value_ctype)
        )
        errors.handle_error(self, error_code)
        return float(value_ctype.value)

    def _set_attribute_vi_real64(self, attribute, value):
        vi_ctype = _visatype.ViSession(self._vi)
        active_item_ctype = _create_string_buffer(self._active_item or "")
        attribute_ctype = _visatype.ViAttr(attribute)
        value_ctype = _visatype.ViReal64(value)
        error_code = self._library.niSync_SetAttributeViReal64(
            vi_ctype, active_item_ctype, attribute_ctype, value_ctype
        )
        errors.handle_error(self, error_code)

    def _get_attribute_vi_boolean(self, attribute):
        vi_ctype = _visatype.ViSession(self._vi)
        active_item_ctype = _create_string_buffer(self._active_item or "")
        attribute_ctype = _visatype.ViAttr(attribute)
        value_ctype = _visatype.ViBoolean()
        error_code = self._library.niSync_GetAttributeViBoolean(
            vi_ctype, active_item_ctype, attribute_ctype, ctypes.pointer(value_ctype)
        )
        errors.handle_error(self, error_code)
        return bool(value_ctype.value)

    def _set_attribute_vi_boolean(self, attribute, value):
        vi_ctype = _visatype.ViSession(self._vi)
        active_item_ctype = _create_string_buffer(self._active_item or "")
        attribute_ctype = _visatype.ViAttr(attribute)
        value_ctype = _visatype.ViBoolean(value)
        error_code = self._library.niSync_SetAttributeViBoolean(
            vi_ctype, active_item_ctype, attribute_ctype, value_ctype
        )
        errors.handle_error(self, error_code)

    def _get_attribute_vi_string(self, attribute):
        vi_ctype = _visatype.ViSession(self._vi)
        active_item_ctype = _create_string_buffer(self._active_item or "")
        attribute_ctype = _visatype.ViAttr(attribute)
        buffer_size_ctype = _visatype.ViInt32(256)
        value_ctype = ctypes.create_string_buffer(buffer_size_ctype.value)
        error_code = self._library.niSync_GetAttributeViString(
            vi_ctype, active_item_ctype, attribute_ctype, buffer_size_ctype, value_ctype
        )
        errors.handle_error(self, error_code)
        return str(value_ctype.value.decode())

    def _set_attribute_vi_string(self, attribute, value):
        vi_ctype = _visatype.ViSession(self._vi)
        active_item_ctype = _create_string_buffer(self._active_item or "")
        attribute_ctype = _visatype.ViAttr(attribute)
        value_ctype = _visatype.ViConstString(value.encode("ascii"))
        error_code = self._library.niSync_SetAttributeViString(
            vi_ctype, active_item_ctype, attribute_ctype, value_ctype
        )
        errors.handle_error(self, error_code)

    def _init(self, resource_name, id_query=False, reset_device=False):
        resource_name_ctype = _create_string_buffer(resource_name)
        id_query_ctype = _visatype.ViBoolean(id_query)
        reset_device_ctype = _visatype.ViBoolean(reset_device)
        vi_ctype = _visatype.ViSession()
        error_code = self._library.niSync_init(
            resource_name_ctype, id_query_ctype, reset_device_ctype, ctypes.pointer(vi_ctype)
        )
        errors.handle_error(self, error_code)
        return int(vi_ctype.value)

    def _close(self):
        vi_ctype = _visatype.ViSession(self._vi)
        error_code = self._library.niSync_close(vi_ctype)
        errors.handle_error(self, error_code)


class Session(_SessionBase):
    """
    Create a new NI-Sync session to the specified in the resource_name parameter.

    :param resource_name: Resource name of the NI-Sync device to initialize.
    :type resource_name: str
    :param id_query: Ignored
    :type id_query: bool
    :param reset_device: Specifies whether to reset the device during the initialization process.


    :type reset_device: bool
    """

    def __init__(self, resource_name, id_query=False, reset_device=False):
        super(Session, self).__init__(vi=None, library=None, active_item=None)
        self._resource_name = resource_name
        self._library = _library_singleton.get()
        self._vi = 0  # This must be set before calling _init().
        self._vi = self._init(resource_name, id_query, reset_device)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        self._close()
        self._vi = 0

    def reset(self):
        vi_ctype = _visatype.ViSession(self._vi)
        error_code = self._library.niSync_reset(vi_ctype)
        errors.handle_error(self, error_code)

    def reset_frequency(self):
        error_code = self._library.niSync_ResetFrequency(self._vi)
        errors.handle_error(self, error_code)

    def connect_trigger_terminals(
        self,
        source,
        destination,
        sync_clock="SyncClkAsync",
        invert=False,
        update_edge=enums.UpdateEdge.RISING,
    ):
        error_code = self._library.niSync_ConnectTrigTerminals(
            self._vi, source, destination, sync_clock, invert, enums.UpdateEdge(update_edge).value
        )
        errors.handle_error(self, error_code)

    route = connect_trigger_terminals

    def disconnect_trigger_terminals(self, source, destination):
        error_code = self._library.niSync_DisconnectTrigTerminals(self._vi, source, destination)
        errors.handle_error(self, error_code)

    unroute = disconnect_trigger_terminals

    def connect_clock_terminals(self, source, destination):
        error_code = self._library.niSync_ConnectClkTerminals(self._vi, source, destination)
        errors.handle_error(self, error_code)

    def disconnect_clock_terminals(self, source, destination):
        error_code = self._library.niSync_DisconnectClkTerminals(self._vi, source, destination)
        errors.handle_error(self, error_code)

    def connect_software_trigger(
        self,
        source,
        destination,
        sync_clock="SyncClkFullSpeed",
        invert=False,
        update_edge=enums.UpdateEdge.RISING,
        delay=0.0,
    ):
        error_code = self._library.niSync_ConnectSWTrigToTerminal(
            self._vi,
            source,
            destination,
            sync_clock,
            invert,
            enums.UpdateEdge(update_edge).value,
            delay,
        )
        errors.handle_error(self, error_code)

    def disconnect_software_trigger(self, source, destination):
        error_code = self._library.niSync_DisconnectSWTrigFromTerminal(
            self._vi, source, destination
        )
        errors.handle_error(self, error_code)

    def send_software_trigger(self, source):
        error_code = self._library.niSync_SendSoftwareTrigger(self._vi, source)
        errors.handle_error(self, error_code)

    def get_time(self):
        """
        Gets the time on the device.
        Returns a timezone-naive datetime in the TAI timescale.
        """

        vi_ctype = _visatype.ViSession(self._vi)
        seconds_ctype = _visatype.ViUInt32()
        nanoseconds_ctype = _visatype.ViUInt32()
        frac_nanoseconds_ctype = _visatype.ViUInt16()
        error_code = self._library.niSync_GetTime(
            vi_ctype,
            ctypes.pointer(seconds_ctype),
            ctypes.pointer(nanoseconds_ctype),
            ctypes.pointer(frac_nanoseconds_ctype),
        )
        errors.handle_error(self, error_code)
        return _tai_time_parts_to_date_time(
            seconds_ctype.value,
            nanoseconds_ctype.value,
            frac_nanoseconds_ctype.value,
        )

    def set_time(self, time_source=enums.InitialTimeSource.SYSTEM_CLK, date_time=None):
        """
        Sets the time on the device.
        date_time is a timezone-naive datetime in the TAI timescale.
        """

        if time_source == enums.InitialTimeSource.SYSTEM_CLK:
            if date_time is not None:
                raise errors.Error(
                    "When calling set_time() with a time_source of SYSTEM_CLK, please pass a date_time of None"
                )
        elif time_source == enums.InitialTimeSource.MANUAL:
            if date_time is None:
                raise errors.Error(
                    "When calling set_time() with a time_source of MANUAL, please pass a valid date_time"
                )
        else:
            raise errors.Error("Invalid time_source " + str(time_source) + " passed to set_time()")
        seconds, nanoseconds, frac_nanoseconds = _date_time_to_tai_time_parts(date_time)
        vi_ctype = _visatype.ViSession(self._vi)
        error_code = self._library.niSync_SetTime(
            vi_ctype, time_source, seconds, nanoseconds, frac_nanoseconds
        )
        errors.handle_error(self, error_code)

    def read_current_temperature(self):
        vi_ctype = _visatype.ViSession(self._vi)
        temperature_ctype = _visatype.ViReal64()
        error_code = self._library.niSync_ReadCurrentTemperature(
            vi_ctype, ctypes.pointer(temperature_ctype)
        )
        errors.handle_error(self, error_code)
        return temperature_ctype.value

    def get_ext_cal_last_temp(self):
        vi_ctype = _visatype.ViSession(self._vi)
        temperature_ctype = _visatype.ViReal64()
        error_code = self._library.niSync_GetExtCalLastTemp(
            vi_ctype, ctypes.pointer(temperature_ctype)
        )
        errors.handle_error(self, error_code)
        return temperature_ctype.value

    def get_ext_cal_last_time(self):
        vi_ctype = _visatype.ViSession(self._vi)
        year_ctype = _visatype.ViInt32()
        month_ctype = _visatype.ViInt32()
        day_ctype = _visatype.ViInt32()
        hour_ctype = _visatype.ViInt32()
        minute_ctype = _visatype.ViInt32()
        error_code = self._library.niSync_GetExtCalLastDateAndTime(
            vi_ctype,
            ctypes.pointer(year_ctype),
            ctypes.pointer(month_ctype),
            ctypes.pointer(day_ctype),
            ctypes.pointer(hour_ctype),
            ctypes.pointer(minute_ctype),
        )
        errors.handle_error(self, error_code)
        return datetime(
            year_ctype.value,
            month_ctype.value,
            day_ctype.value,
            hour_ctype.value,
            minute_ctype.value,
            second=0,
            tzinfo=timezone.utc,
        )

    def get_location(self):
        vi_ctype = _visatype.ViSession(self._vi)
        latitude_ctype = _visatype.ViReal64()
        longitude_ctype = _visatype.ViReal64()
        altitude_ctype = _visatype.ViReal64()

        error_code = self._library.niSync_GetLocation(
            vi_ctype,
            ctypes.pointer(latitude_ctype),
            ctypes.pointer(longitude_ctype),
            ctypes.pointer(altitude_ctype),
        )
        errors.handle_error(self, error_code)
        return latitude_ctype.value, longitude_ctype.value, altitude_ctype.value

    def get_velocity(self):
        vi_ctype = _visatype.ViSession(self._vi)
        east_velocity_ctype = _visatype.ViReal64()
        north_velocity_ctype = _visatype.ViReal64()
        up_velocity_ctype = _visatype.ViReal64()

        error_code = self._library.niSync_GetVelocity(
            vi_ctype,
            ctypes.pointer(east_velocity_ctype),
            ctypes.pointer(north_velocity_ctype),
            ctypes.pointer(up_velocity_ctype),
        )
        errors.handle_error(self, error_code)
        return east_velocity_ctype.value, north_velocity_ctype.value, up_velocity_ctype.value

    def create_future_time_event(self, terminal, level=enums.Level.LOW, time=None):
        seconds, nanoseconds, frac_nanoseconds = _date_time_to_tai_time_parts(time)
        error_code = self._library.niSync_CreateFutureTimeEvent(
            self._vi, terminal, enums.Level(level).value, seconds, nanoseconds, frac_nanoseconds
        )
        errors.handle_error(self, error_code)

    def clear_future_time_events(self, terminal):
        error_code = self._library.niSync_ClearFutureTimeEvents(self._vi, terminal)
        errors.handle_error(self, error_code)

    def enable_timestamp_trigger(self, terminal, active_edge=enums.Edge.RISING, decimation=None):
        if decimation is None:
            error_code = self._library.niSync_EnableTimeStampTrigger(
                self._vi, terminal, enums.Edge(active_edge).value
            )
        else:
            error_code = self._library.niSync_EnableTimeStampTriggerWithDecimation(
                self._vi, terminal, enums.Edge(active_edge).value, decimation
            )
        errors.handle_error(self, error_code)

    def read_trigger_timestamp(self, terminal, timeout=10.0):
        seconds_ctype = _visatype.ViUInt32()
        nanoseconds_ctype = _visatype.ViUInt32()
        frac_nanoseconds_ctype = _visatype.ViUInt16()
        detected_edge_ctype = _visatype.ViInt32()
        error_code = self._library.niSync_ReadTriggerTimeStamp(
            self._vi,
            terminal,
            timeout,
            ctypes.pointer(seconds_ctype),
            ctypes.pointer(nanoseconds_ctype),
            ctypes.pointer(frac_nanoseconds_ctype),
            ctypes.pointer(detected_edge_ctype),
        )
        errors.handle_error(self, error_code)
        return (
            _tai_time_parts_to_date_time(
                seconds_ctype.value,
                nanoseconds_ctype.value,
                frac_nanoseconds_ctype,
            ),
            enums.Edge(detected_edge_ctype.value),
        )

    def read_multiple_trigger_timestamp(self, terminal, count=1, timeout=10.0):
        int32_array, uint32_array, uint16_array = (
            _visatype.ViInt32 * count,
            _visatype.ViUInt32 * count,
            _visatype.ViUInt16 * count,
        )
        seconds = uint32_array()
        nanoseconds = uint32_array()
        frac_nanoseconds = uint16_array()
        detected_edges = int32_array()
        timestamps_read = _visatype.ViUInt32()
        error_code = self._library.niSync_ReadMultipleTriggerTimeStamp(
            self._vi,
            terminal,
            count,
            timeout,
            seconds,
            nanoseconds,
            frac_nanoseconds,
            detected_edges,
            ctypes.pointer(timestamps_read),
        )
        errors.handle_error(self, error_code)
        return [
            (
                _tai_time_parts_to_date_time(seconds[i], nanoseconds[i], frac_nanoseconds[i]),
                enums.Edge(detected_edges[i]),
            )
            for i in range(timestamps_read.value)
        ]

    def disable_timestamp_trigger(self, terminal):
        error_code = self._library.niSync_DisableTimeStampTrigger(self._vi, terminal)
        errors.handle_error(self, error_code)

    def create_clock(self, terminal, high_ticks, low_ticks, start_time=None, stop_time=None):
        error_code = self._library.niSync_CreateClock(
            self._vi,
            terminal,
            high_ticks,
            low_ticks,
            *(_date_time_to_tai_time_parts(start_time) + _date_time_to_tai_time_parts(stop_time))
        )
        errors.handle_error(self, error_code)

    def clear_clock(self, terminal):
        error_code = self._library.niSync_ClearClock(self._vi, terminal)
        errors.handle_error(self, error_code)

    def persist_config(self):
        error_code = self._library.niSync_PersistConfig(self._vi)
        errors.handle_error(self, error_code)

    def self_test(self):
        vi_ctype = _visatype.ViSession(self._vi)
        result_ctype = _visatype.ViInt16()
        message_ctype = ctypes.create_string_buffer(256)
        error_code = self._library.niSync_self_test(
            vi_ctype, ctypes.pointer(result_ctype), message_ctype
        )
        errors.handle_error(self, error_code)
        return result_ctype.value, message_ctype.value.decode()

    def set_timereference_freerunning(self):
        error_code = self._library.niSync_SetTimeReferenceFreeRunning(self._vi)
        errors.handle_error(self, error_code)

    def set_timereference_1588(self):
        error_code = self._library.niSync_SetTimeReference1588OrdinaryClock(self._vi)
        errors.handle_error(self, error_code)

    def set_timereference_8021as(self):
        error_code = self._library.niSync_SetTimeReference8021AS(self._vi)
        errors.handle_error(self, error_code)

    def set_timereference_irig(self, irig_type, terminal):
        error_code = self._library.niSync_SetTimeReferenceIRIG(self._vi, irig_type, terminal)
        errors.handle_error(self, error_code)

    def set_timereference_gps(self):
        error_code = self._library.niSync_SetTimeReferenceGPS(self._vi)
        errors.handle_error(self, error_code)

    def set_timereference_pps(self, terminal, initial_time=None):
        use_manual_time = False
        initial_time_seconds, initial_time_nanoseconds, initial_time_fractional_nanoseconds = (
            0,
            0,
            0,
        )

        if initial_time:
            if initial_time < tai_epoch_no_tz:
                raise errors.Error(
                    "Setting board time before TAI epoch of 1 January 1970 is not allowed"
                )
            use_manual_time = True
            initial_time_seconds, initial_time_nanoseconds, initial_time_fractional_nanoseconds = (
                _date_time_to_tai_time_parts(initial_time)
            )

        error_code = self._library.niSync_SetTimeReferencePPS(
            self._vi,
            terminal,
            use_manual_time,
            initial_time_seconds,
            initial_time_nanoseconds,
            initial_time_fractional_nanoseconds,
        )
        errors.handle_error(self, error_code)

    def read_last_gps_timestamp(self):
        vi_ctype = _visatype.ViSession(self._vi)
        timestamp_seconds_ctype = _visatype.ViUInt32()
        timestamp_nanoseconds_ctype = _visatype.ViUInt32()
        timestamp_fractional_nanoseconds_ctype = _visatype.ViUInt16()
        gps_seconds_ctype = _visatype.ViUInt32()
        gps_nanoseconds_ctype = _visatype.ViUInt32()
        gps_fractional_nanoseconds_ctype = _visatype.ViUInt16()
        error_code = self._library.niSync_ReadLastGPSTimestamp(
            vi_ctype,
            timestamp_seconds_ctype,
            timestamp_nanoseconds_ctype,
            timestamp_fractional_nanoseconds_ctype,
            gps_seconds_ctype,
            gps_nanoseconds_ctype,
            gps_fractional_nanoseconds_ctype,
        )
        errors.handle_error(self, error_code)
        return (
            _tai_time_parts_to_date_time(
                timestamp_seconds_ctype.value,
                timestamp_nanoseconds_ctype.value,
                timestamp_fractional_nanoseconds_ctype.value,
            ),
            _tai_time_parts_to_date_time(
                gps_seconds_ctype.value,
                gps_nanoseconds_ctype.value,
                gps_fractional_nanoseconds_ctype.value,
            ),
        )

    def enable_gps_timestamping(self):
        error_code = self._library.niSync_EnableGPSTimestamping(self._vi)
        errors.handle_error(self, error_code)

    def disable_gps_timestamping(self):
        error_code = self._library.niSync_DisableGPSTimestamping(self._vi)
        errors.handle_error(self, error_code)

    def read_last_irig_timestamp(self, terminal="PFI0"):
        vi_ctype = _visatype.ViSession(self._vi)
        timestamp_seconds_ctype = _visatype.ViUInt32()
        timestamp_nanoseconds_ctype = _visatype.ViUInt32()
        timestamp_fractional_nanoseconds_ctype = _visatype.ViUInt16()
        irig_seconds_ctype = _visatype.ViUInt32()
        irig_nanoseconds_ctype = _visatype.ViUInt32()
        irig_fractional_nanoseconds_ctype = _visatype.ViUInt16()
        error_code = self._library.niSync_ReadLastIRIGTimestamp(
            vi_ctype,
            terminal,
            timestamp_seconds_ctype,
            timestamp_nanoseconds_ctype,
            timestamp_fractional_nanoseconds_ctype,
            irig_seconds_ctype,
            irig_nanoseconds_ctype,
            irig_fractional_nanoseconds_ctype,
        )
        errors.handle_error(self, error_code)
        return (
            _tai_time_parts_to_date_time(
                timestamp_seconds_ctype.value,
                timestamp_nanoseconds_ctype.value,
                timestamp_fractional_nanoseconds_ctype.value,
            ),
            _tai_time_parts_to_date_time(
                irig_seconds_ctype.value,
                irig_nanoseconds_ctype.value,
                irig_fractional_nanoseconds_ctype.value,
            ),
        )

    def enable_irig_timestamping(self, irig_type, terminal="PFI0"):
        error_code = self._library.niSync_EnableIRIGTimestamping(self._vi, irig_type, terminal)
        errors.handle_error(self, error_code)

    def disable_irig_timestamping(self, terminal="PFI0"):
        error_code = self._library.niSync_DisableIRIGTimestamping(self._vi, terminal)
        errors.handle_error(self, error_code)

    def start_1588(self):
        error_code = self._library.niSync_Start1588(self._vi)
        errors.handle_error(self, error_code)

    def stop_1588(self):
        error_code = self._library.niSync_Stop1588(self._vi)
        errors.handle_error(self, error_code)

    def start_8021as(self):
        error_code = self._library.niSync_Start8021AS(self._vi)
        errors.handle_error(self, error_code)

    def stop_8021as(self):
        error_code = self._library.niSync_Stop8021AS(self._vi)
        errors.handle_error(self, error_code)

    def measure_frequency(self, terminal, duration=0.00000100):
        actual_duration_ctype = _visatype.ViReal64()
        frequency_ctype = _visatype.ViReal64()
        frequency_error_ctype = _visatype.ViReal64()
        error_code = self._library.niSync_MeasureFrequency(
            self._vi,
            terminal,
            duration,
            actual_duration_ctype,
            frequency_ctype,
            frequency_error_ctype,
        )
        errors.handle_error(self, error_code)
        return actual_duration_ctype.value, frequency_ctype.value, frequency_error_ctype.value

    def measure_frequency_ex(self, terminal, duration=0.00000100, decimation_count=1):
        actual_duration_ctype = _visatype.ViReal64()
        frequency_ctype = _visatype.ViReal64()
        frequency_error_ctype = _visatype.ViReal64()
        error_code = self._library.niSync_MeasureFrequencyEx(
            self._vi,
            terminal,
            duration,
            decimation_count,
            actual_duration_ctype,
            frequency_ctype,
            frequency_error_ctype,
        )
        errors.handle_error(self, error_code)
        return actual_duration_ctype.value, frequency_ctype.value, frequency_error_ctype.value

    def revision_query(self):
        vi_ctype = _visatype.ViSession(self._vi)
        instrument_driver_revision_ctype = ctypes.create_string_buffer(256)
        firmware_revision_ctype = ctypes.create_string_buffer(256)
        error_code = self._library.niSync_revision_query(
            vi_ctype, instrument_driver_revision_ctype, firmware_revision_ctype
        )
        errors.handle_error(self, error_code)
        return (
            instrument_driver_revision_ctype.value.decode(),
            firmware_revision_ctype.value.decode(),
        )

    @property
    def time_reference_names(self):
        vi_ctype = _visatype.ViSession(self._vi)
        buffer_size_ctype = _visatype.ViUInt32(0)
        names_ctype = None
        buffer_size = self._library.niSync_GetTimeReferenceNames(
            vi_ctype, buffer_size_ctype, names_ctype
        )
        if buffer_size < 0:
            errors.handle_error(self, buffer_size)
        buffer_size_ctype = _visatype.ViUInt32(buffer_size)
        names_ctype = ctypes.create_string_buffer(buffer_size)
        error_code = self._library.niSync_GetTimeReferenceNames(
            vi_ctype, buffer_size_ctype, names_ctype
        )
        errors.handle_error(self, error_code)
        return names_ctype.value.decode().split(",")

    @property
    def time_references(self):
        """
        Returns a list of :class:`~nisync.session.TimeReference` objects
        """
        return [self(name) for name in self.time_reference_names]

    @property
    def resource_name(self):
        return self._resource_name


class TimeReference(object):
    def __init__(self, session):
        self._session = session
        self._ports = None

    @property
    def name(self):
        """
        Returns the name of the time references instance.
        """
        return self._session._active_item

    @property
    def ports(self):
        class PortSession(_SessionBase):
            pass

        if self._ports is None:
            self._ports = []
            num_ports = 1
            tr_type = self._session.time_reference_type
            if tr_type == "IEEE 802.1AS-2011 TAB" or tr_type == "IEEE 1588-2008 BC":
                num_ports = 2
            for _ in range(num_ports):
                session = PortSession(
                    self._session._vi, self._session._library, self._session._active_item
                )
                if tr_type.startswith("IEEE 1588-2008"):
                    self._ports.append(IEEE1588Port(session))
                if tr_type.startswith("IEEE 802.1AS-2011"):
                    self._ports.append(IEEE8021ASPort(session))
        return self._ports

    @property
    def present(self):
        return self._session.time_reference_present

    @present.setter
    def present(self, value):
        self._session.time_reference_present = value

    @property
    def current(self):
        return self._session.time_reference_current

    @current.setter
    def current(self, value):
        self._session.time_reference_current = value

    @property
    def offset(self):
        return self._session.time_reference_offset

    @offset.setter
    def offset(self, value):
        self._session.time_reference_offset = value

    @property
    def utc_offset(self):
        return self._session.time_reference_utc_offset

    @utc_offset.setter
    def utc_offset(self, value):
        self._session.time_reference_utc_offset = value

    @property
    def utc_offset_valid(self):
        return self._session.time_reference_utc_offset_valid

    @utc_offset_valid.setter
    def utc_offset_valid(self, value):
        self._session.time_reference_utc_offset_valid = value

    @property
    def last_sync_id(self):
        return self._session.time_reference_last_sync_id

    @last_sync_id.setter
    def last_sync_id(self, value):
        self._session.time_reference_last_sync_id = value

    @property
    def offset_ns(self):
        return self._session.time_reference_offset_ns

    @offset_ns.setter
    def offset_ns(self, value):
        self._session.time_reference_offset_ns = value

    @property
    def type(self):
        return self._session.time_reference_type

    @type.setter
    def type(self, value):
        self._session.time_reference_type = value

    @property
    def enabled(self):
        return self._session.time_reference_enabled

    @enabled.setter
    def enabled(self, value):
        self._session.time_reference_enabled = value

    @property
    def is_selected(self):
        return self._session.time_reference_is_selected

    @is_selected.setter
    def is_selected(self, value):
        self._session.time_reference_is_selected = value


class IEEE1588TimeReference(TimeReference):

    @property
    def ip_address(self):
        return self._session.ieee_1588_ip_address

    @ip_address.setter
    def ip_address(self, value):
        self._session.ieee_1588_ip_address = value

    @property
    def steps_to_grandmaster(self):
        return self._session.ieee_1588_steps_to_grandmaster

    @steps_to_grandmaster.setter
    def steps_to_grandmaster(self, value):
        self._session.ieee_1588_steps_to_grandmaster = value

    @property
    def clock_id(self):
        return self._session.ieee_1588_clock_id

    @clock_id.setter
    def clock_id(self, value):
        self._session.ieee_1588_clock_id = value

    @property
    def clock_class(self):
        return self._session.ieee_1588_clock_class

    @clock_class.setter
    def clock_class(self, value):
        self._session.ieee_1588_clock_class = value

    @property
    def clock_accuracy(self):
        return self._session.ieee_1588_clock_accuracy

    @clock_accuracy.setter
    def clock_accuracy(self, value):
        self._session.ieee_1588_clock_accuracy = value

    @property
    def priority1(self):
        return self._session.ieee_1588_priority1

    @priority1.setter
    def priority1(self, value):
        self._session.ieee_1588_priority1 = value

    @property
    def priority2(self):
        return self._session.ieee_1588_priority2

    @priority2.setter
    def priority2(self, value):
        self._session.ieee_1588_priority2 = value

    @property
    def grandmaster_clock_id(self):
        return self._session.ieee_1588_grandmaster_clock_id

    @grandmaster_clock_id.setter
    def grandmaster_clock_id(self, value):
        self._session.ieee_1588_grandmaster_clock_id = value

    @property
    def grandmaster_clock_class(self):
        return self._session.ieee_1588_grandmaster_clock_class

    @grandmaster_clock_class.setter
    def grandmaster_clock_class(self, value):
        self._session.ieee_1588_grandmaster_clock_class = value

    @property
    def grandmaster_clock_accuracy(self):
        return self._session.ieee_1588_grandmaster_clock_accuracy

    @grandmaster_clock_accuracy.setter
    def grandmaster_clock_accuracy(self, value):
        self._session.ieee_1588_grandmaster_clock_accuracy = value

    @property
    def grandmaster_priority1(self):
        return self._session.ieee_1588_grandmaster_priority1

    @grandmaster_priority1.setter
    def grandmaster_priority1(self, value):
        self._session.ieee_1588_grandmaster_priority1 = value

    @property
    def grandmaster_priority2(self):
        return self._session.ieee_1588_grandmaster_priority2

    @grandmaster_priority2.setter
    def grandmaster_priority2(self, value):
        self._session.ieee_1588_grandmaster_priority2 = value

    @property
    def mean_path_delay(self):
        return self._session.ieee_1588_mean_path_delay

    @mean_path_delay.setter
    def mean_path_delay(self, value):
        self._session.ieee_1588_mean_path_delay = value

    @property
    def grandmaster_ip_address(self):
        return self._session.ieee_1588_grandmaster_ip_address

    @grandmaster_ip_address.setter
    def grandmaster_ip_address(self, value):
        self._session.ieee_1588_grandmaster_ip_address = value

    @property
    def bmca_mode(self):
        return self._session.ieee_1588_bmca_mode

    @bmca_mode.setter
    def bmca_mode(self, value):
        self._session.ieee_1588_bmca_mode = value

    @property
    def offset_scaled_log_variance(self):
        return self._session.ieee_1588_offset_scaled_log_variance

    @offset_scaled_log_variance.setter
    def offset_scaled_log_variance(self, value):
        self._session.ieee_1588_offset_scaled_log_variance = value

    @property
    def leap59(self):
        return self._session.ieee_1588_leap59

    @leap59.setter
    def leap59(self, value):
        self._session.ieee_1588_leap59 = value

    @property
    def leap61(self):
        return self._session.ieee_1588_leap61

    @leap61.setter
    def leap61(self, value):
        self._session.ieee_1588_leap61 = value

    @property
    def time_traceable(self):
        return self._session.ieee_1588_time_traceable

    @time_traceable.setter
    def time_traceable(self, value):
        self._session.ieee_1588_time_traceable = value

    @property
    def frequency_traceable(self):
        return self._session.ieee_1588_frequency_traceable

    @frequency_traceable.setter
    def frequency_traceable(self, value):
        self._session.ieee_1588_frequency_traceable = value

    @property
    def time_source(self):
        return self._session.ieee_1588_time_source

    @time_source.setter
    def time_source(self, value):
        self._session.ieee_1588_time_source = value


class IEEE8021ASTimeReference(TimeReference):

    @property
    def clock_id(self):
        return self._session.ieee_8021as_clock_id

    @clock_id.setter
    def clock_id(self, value):
        self._session.ieee_8021as_clock_id = value

    @property
    def clock_class(self):
        return self._session.ieee_8021as_clock_class

    @clock_class.setter
    def clock_class(self, value):
        self._session.ieee_8021as_clock_class = value

    @property
    def clock_accuracy(self):
        return self._session.ieee_8021as_clock_accuracy

    @clock_accuracy.setter
    def clock_accuracy(self, value):
        self._session.ieee_8021as_clock_accuracy = value

    @property
    def priority1(self):
        return self._session.ieee_8021as_priority1

    @priority1.setter
    def priority1(self, value):
        self._session.ieee_8021as_priority1 = value

    @property
    def priority2(self):
        return self._session.ieee_8021as_priority2

    @priority2.setter
    def priority2(self, value):
        self._session.ieee_8021as_priority2 = value

    @property
    def grandmaster_clock_id(self):
        return self._session.ieee_8021as_grandmaster_clock_id

    @grandmaster_clock_id.setter
    def grandmaster_clock_id(self, value):
        self._session.ieee_8021as_grandmaster_clock_id = value

    @property
    def grandmaster_clock_class(self):
        return self._session.ieee_8021as_grandmaster_clock_class

    @grandmaster_clock_class.setter
    def grandmaster_clock_class(self, value):
        self._session.ieee_8021as_grandmaster_clock_class = value

    @property
    def grandmaster_clock_accuracy(self):
        return self._session.ieee_8021as_grandmaster_clock_accuracy

    @grandmaster_clock_accuracy.setter
    def grandmaster_clock_accuracy(self, value):
        self._session.ieee_8021as_grandmaster_clock_accuracy = value

    @property
    def grandmaster_priority1(self):
        return self._session.ieee_8021as_grandmaster_priority1

    @grandmaster_priority1.setter
    def grandmaster_priority1(self, value):
        self._session.ieee_8021as_grandmaster_priority1 = value

    @property
    def grandmaster_priority2(self):
        return self._session.ieee_8021as_grandmaster_priority2

    @grandmaster_priority2.setter
    def grandmaster_priority2(self, value):
        self._session.ieee_8021as_grandmaster_priority2 = value


class GPSTimeReference(TimeReference):

    @property
    def antenna_connected(self):
        return self._session.gps_antenna_connected

    @antenna_connected.setter
    def antenna_connected(self, value):
        self._session.gps_antenna_connected = value

    @property
    def recalculate_position(self):
        return self._session.gps_recalculate_position

    @recalculate_position.setter
    def recalculate_position(self, value):
        self._session.gps_recalculate_position = value

    @property
    def satellites_available(self):
        return self._session.gps_satellites_available

    @satellites_available.setter
    def satellites_available(self, value):
        self._session.gps_satellites_available = value

    @property
    def self_survey(self):
        return self._session.gps_self_survey

    @self_survey.setter
    def self_survey(self, value):
        self._session.gps_self_survey = value

    @property
    def mobile_mode(self):
        return self._session.gps_mobile_mode

    @mobile_mode.setter
    def mobile_mode(self, value):
        self._session.gps_mobile_mode = value

    @property
    def status(self):
        return self._session.gps_status

    @status.setter
    def status(self, value):
        self._session.gps_status = value


class IRIGBTimeReference(TimeReference):
    pass


class EtherCATTimeReference(TimeReference):
    pass


class PPSTimeReference(TimeReference):
    pass


class Port(object):
    def __init__(self, session):
        self._session = session


class IEEE1588Port(Port):

    @property
    def port_state(self):
        return self._session.ieee_1588_port_state

    @port_state.setter
    def port_state(self, value):
        self._session.ieee_1588_port_state = value

    @property
    def log_sync_interval(self):
        return self._session.ieee_1588_log_sync_interval

    @log_sync_interval.setter
    def log_sync_interval(self, value):
        self._session.ieee_1588_log_sync_interval = value

    @property
    def interface_name(self):
        return self._session.ieee_1588_interface_name

    @interface_name.setter
    def interface_name(self, value):
        self._session.ieee_1588_interface_name = value


class IEEE8021ASPort(Port):

    @property
    def port_state(self):
        return self._session.ieee_8021as_port_state

    @port_state.setter
    def port_state(self, value):
        self._session.ieee_8021as_port_state = value

    @property
    def log_sync_interval(self):
        return self._session.ieee_8021as_log_sync_interval

    @log_sync_interval.setter
    def log_sync_interval(self, value):
        self._session.ieee_8021as_log_sync_interval = value

    @property
    def log_announce_interval(self):
        return self._session.ieee_8021as_log_announce_interval

    @log_announce_interval.setter
    def log_announce_interval(self, value):
        self._session.ieee_8021as_log_announce_interval = value

    @property
    def interface_name(self):
        return self._session.ieee_8021as_interface_name

    @interface_name.setter
    def interface_name(self, value):
        self._session.ieee_8021as_interface_name = value

    @property
    def neighbor_prop_delay_thresh(self):
        return self._session.ieee_8021as_neighbor_prop_delay_thresh

    @neighbor_prop_delay_thresh.setter
    def neighbor_prop_delay_thresh(self, value):
        self._session.ieee_8021as_neighbor_prop_delay_thresh = value

    @property
    def as_capable(self):
        return self._session.ieee_8021as_as_capable

    @as_capable.setter
    def as_capable(self, value):
        self._session.ieee_8021as_as_capable = value
