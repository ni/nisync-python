import datetime
import math
from decimal import Decimal

import hightime
import pytest

from nisync.session import (
    _date_time_to_tai_time_parts,
    _tai_time_parts_to_date_time,
    _tai_time_to_tai_timestamp,
    _tai_timestamp_to_tai_time,
)

# for precision tests, define a small and large timestamp and their corresponding datetimes
SMALL_TIMESTAMP = 2**9
LARGE_TIMESTAMP = 2**37
SMALL_DATE_YEAR = 1970
SMALL_DATE_MONTH = 1
SMALL_DATE_DAY = 1
SMALL_DATE_HOUR = 0
SMALL_DATE_MINUTE = 8
SMALL_DATE_SECOND = 32
LARGE_DATE_YEAR = 6325
LARGE_DATE_MONTH = 4
LARGE_DATE_DAY = 8
LARGE_DATE_HOUR = 15
LARGE_DATE_MINUTE = 4
LARGE_DATE_SECOND = 32
DATETIMES = {
    "small": {
        "timestamp": SMALL_TIMESTAMP,
        "datetime": datetime.datetime(
            year=SMALL_DATE_YEAR,
            month=SMALL_DATE_MONTH,
            day=SMALL_DATE_DAY,
            hour=SMALL_DATE_HOUR,
            minute=SMALL_DATE_MINUTE,
            second=SMALL_DATE_SECOND,
        ),
        "hightime": hightime.datetime(
            year=SMALL_DATE_YEAR,
            month=SMALL_DATE_MONTH,
            day=SMALL_DATE_DAY,
            hour=SMALL_DATE_HOUR,
            minute=SMALL_DATE_MINUTE,
            second=SMALL_DATE_SECOND,
        ),
    },
    "large": {
        "timestamp": LARGE_TIMESTAMP,
        "datetime": datetime.datetime(
            year=LARGE_DATE_YEAR,
            month=LARGE_DATE_MONTH,
            day=LARGE_DATE_DAY,
            hour=LARGE_DATE_HOUR,
            minute=LARGE_DATE_MINUTE,
            second=LARGE_DATE_SECOND,
        ),
        "hightime": hightime.datetime(
            year=LARGE_DATE_YEAR,
            month=LARGE_DATE_MONTH,
            day=LARGE_DATE_DAY,
            hour=LARGE_DATE_HOUR,
            minute=LARGE_DATE_MINUTE,
            second=LARGE_DATE_SECOND,
        ),
    },
}


def _get_base_date(date_size, date_type):
    base_timestamp = DATETIMES[date_size]["timestamp"]
    base_datetime = DATETIMES[date_size][date_type]
    return base_timestamp, base_datetime


def _get_expected_tai_time(date_size, expected_tai_timestamp):
    _, microseconds = map(
        Decimal, divmod(Decimal(expected_tai_timestamp) * Decimal(1e6), Decimal(1e6))
    )
    # use only hightime here since _tai_timestamp_to_tai_time() returns hightime
    return DATETIMES[date_size]["hightime"] + hightime.timedelta(microseconds=microseconds)


@pytest.mark.parametrize("decimal_type", [Decimal, float], ids=["Decimal", "float"])
@pytest.mark.parametrize(
    "starting_fractional_seconds", [1e-6, 1e-9], ids=["microsecond", "nanosecond"]
)
@pytest.mark.parametrize(
    "date_type",
    [
        "datetime",
        "hightime",
    ],
    ids=["datetime", "hightime"],
)
@pytest.mark.parametrize("date_size", ["small", "large"], ids=["small", "large"])
def test_tai_timestamp_round_trip(date_size, date_type, starting_fractional_seconds, decimal_type):
    base_timestamp, base_datetime = _get_base_date(date_size, date_type)
    starting_tai_timestamp = decimal_type(base_timestamp) + decimal_type(
        starting_fractional_seconds
    )
    expected_tai_timestamp = Decimal(base_timestamp) + Decimal(starting_fractional_seconds)
    if date_type == "hightime" and decimal_type == "Decimal":
        # nanosecond precision
        precision = 1e-9
    else:
        # microsecond precision
        precision = 1e-6
        # date_type is datetime, so mimic standard datetime's use of float
        # or
        # decimal_type is float, so use float
        expected_tai_timestamp = float(expected_tai_timestamp)
    expected_tai_time = _get_expected_tai_time(date_size, expected_tai_timestamp)

    tai_time = _tai_timestamp_to_tai_time(starting_tai_timestamp)
    diff_seconds = (tai_time - expected_tai_time).total_seconds()
    assert math.isclose(diff_seconds, 0.0, rel_tol=0.0, abs_tol=precision)
    tai_timestamp = _tai_time_to_tai_timestamp(tai_time)
    assert math.isclose(tai_timestamp, starting_tai_timestamp, rel_tol=precision)


@pytest.mark.parametrize(
    "starting_fractional_seconds", [1e-6, 1e-9], ids=["microsecond", "nanosecond"]
)
@pytest.mark.parametrize(
    "date_type",
    [
        "datetime",
        "hightime",
    ],
    ids=["datetime", "hightime"],
)
@pytest.mark.parametrize("date_size", ["small", "large"], ids=["small", "large"])
def test_tai_time_round_trip(date_size, date_type, starting_fractional_seconds):
    base_timestamp, base_datetime = _get_base_date(date_size, date_type)
    expected_tai_timestamp = Decimal(base_timestamp) + Decimal(starting_fractional_seconds)
    expected_tai_time = _get_expected_tai_time(date_size, expected_tai_timestamp)
    if date_type == "hightime":
        starting_tai_time = base_datetime + hightime.timedelta(
            microseconds=starting_fractional_seconds * 1e6
        )
        # nanosecond precision
        precision = 1e-9
    else:
        starting_tai_time = base_datetime + datetime.timedelta(
            microseconds=starting_fractional_seconds * 1e6
        )
        # microsecond precision
        precision = 1e-6

    tai_timestamp = _tai_time_to_tai_timestamp(starting_tai_time)
    assert math.isclose(tai_timestamp, expected_tai_timestamp, rel_tol=precision)
    tai_time = _tai_timestamp_to_tai_time(tai_timestamp)
    diff_seconds = (tai_time - expected_tai_time).total_seconds()
    assert math.isclose(diff_seconds, 0.0, rel_tol=0.0, abs_tol=precision)


@pytest.mark.parametrize("starting_nanoseconds", [1000, 1], ids=["microsecond", "nanosecond"])
@pytest.mark.parametrize(
    "date_type",
    ["hightime"],  # use only hightime here since _tai_time_parts_to_date_time() returns hightime
    ids=["hightime"],
)
@pytest.mark.parametrize("date_size", ["small", "large"], ids=["small", "large"])
def test_tai_time_parts_round_trip(date_size, date_type, starting_nanoseconds):
    base_timestamp, base_datetime = _get_base_date(date_size, date_type)
    expected_tai_timestamp = Decimal(base_timestamp) + Decimal(starting_nanoseconds / 1e9)
    expected_tai_time = _get_expected_tai_time(date_size, expected_tai_timestamp)

    tai_time = _tai_time_parts_to_date_time(base_timestamp, starting_nanoseconds, 0)
    assert tai_time == expected_tai_time
    seconds, nanoseconds, frac_nanoseconds = _date_time_to_tai_time_parts(tai_time)
    assert seconds == base_timestamp
    assert nanoseconds == starting_nanoseconds
    assert frac_nanoseconds == 0
