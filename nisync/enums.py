# This file was generated

from enum import IntEnum


class CtypesEnum(IntEnum):
    @classmethod
    def from_param(cls, obj):
        return int(obj)


class BMCAMode(CtypesEnum):
    SLAVE_ONLY = 0
    MASTER_SLAVE = 1


class Edge(CtypesEnum):
    RISING = 0
    FALLING = 1
    ANY = 2


class ExternalCalibrationAction(CtypesEnum):
    ABORT = 0
    COMMIT = 1


class GPSStatus(CtypesEnum):
    UNINITIALIZED = 0
    ANTENNA_ERROR = 1
    NO_USEABLE_SATELLITE = 2
    ONE_USEABLE_SATELLITE = 3
    TWO_USEABLE_SATELLITES = 4
    THREE_USEABLE_SATELLITES = 5
    NO_GPS_TIME = 6
    PDOP_TOO_HIGH = 7
    UNUSABLE_SATELLITE = 8
    UNUSEABLE_SATELLITE = 8
    FIX_REJECTED = 9
    SELF_SURVEY_COMPLETE = 10
    SELF_SURVEY_NOT_COMPLETE = 11


class IEEE1588ClockAccuracy(CtypesEnum):
    UNKNOWN = 0
    WITHIN_25_NSEC = 1
    WITHIN_100_NSEC = 2
    WITHIN_250_NSEC = 3
    WITHIN_1_USEC = 4
    WITHIN_2500_NSEC = 5
    WITHIN_10_USEC = 6
    WITHIN_25_USEC = 7
    WITHIN_100_USEC = 8
    WITHIN_250_USEC = 9
    WITHIN_1_MSEC = 10
    WITHIN_2500_USEC = 11
    WITHIN_10_MSEC = 12
    WITHIN_25_MSEC = 13
    WITHIN_100_MSEC = 14
    WITHIN_250_MSEC = 15
    WITHIN_1_SEC = 16
    WITHIN_10_SEC = 17
    GREATER_THAN_10_SEC = 18


class IEEE1588ClockClass(CtypesEnum):
    DEFAULT = 248


class IEEE1588PortState(CtypesEnum):
    NOT_DEFINED = -1
    INIT = 0
    FAULT = 1
    DISABLE = 2
    LISTENING = 3
    PREMASTER = 4
    MASTER = 5
    PASSIVE = 6
    UNCALIBRATED = 7
    SLAVE = 8
    STOPPED = 9


class IEEE8021ASClockAccuracy(CtypesEnum):
    WITHIN_25_NSEC = 32
    WITHIN_100_NSEC = 33
    WITHIN_250_NSEC = 34
    WITHIN_1_USEC = 35
    WITHIN_2500_NSEC = 36
    WITHIN_10_USEC = 37
    WITHIN_25_USEC = 38
    WITHIN_100_USEC = 39
    WITHIN_250_USEC = 40
    WITHIN_1_MSEC = 41
    WITHIN_2500_USEC = 42
    WITHIN_10_MSEC = 43
    WITHIN_25_MSEC = 44
    WITHIN_100_MSEC = 45
    WITHIN_250_MSEC = 46
    WITHIN_1_SEC = 47
    WITHIN_10_SEC = 48
    GREATER_THAN_10_SEC = 49
    UNKNOWN = 254


class IEEE8021ASPortState(CtypesEnum):
    DISABLED = 3
    MASTER = 6
    PASSIVE = 7
    SLAVE = 9


class IRIGType(CtypesEnum):
    IRIGB_DC = 0
    IRIGB_AM = 1


class InitialTimeSource(CtypesEnum):
    SYSTEM_CLK = 0
    MANUAL = 1


class Level(CtypesEnum):
    LOW = 0
    HIGH = 1


class SyncInterval(CtypesEnum):
    _125_MSEC = -3
    _250_MSEC = -2
    HALF_SEC = -1
    ONE_SEC = 0
    TWO_SEC = 1


class TimeReference(CtypesEnum):
    GPS = 0
    IRIG = 1
    PPS = 2
    IEEE_1588_ORDINARY_CLOCK = 3
    FREERUNNING = 4
    IEEE_8021AS = 5


class UpdateEdge(CtypesEnum):
    RISING = 0
    FALLING = 1
