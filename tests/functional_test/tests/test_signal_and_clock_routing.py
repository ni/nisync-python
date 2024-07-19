import pytest

from nisync.constants import OSCILLATOR, PXI_CLK10_IN


@pytest.mark.parametrize("source, destination", [(OSCILLATOR, PXI_CLK10_IN)])
def test_signal_and_clock_routing(get_sync_session, source, destination):
    if source != OSCILLATOR:
        raise ValueError("Invalid source")
    else:
        get_sync_session.connect_clock_terminals(source, destination)
