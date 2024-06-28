# This file was generated


class TimeReference(object):
    def __init__(self, session):
        self._session = session

    @property
    def name(self):
        """
        Returns the name of the time references instance.
        """
        return self._session._active_item

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
