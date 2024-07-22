import pytest

from nisync.constants import OSCILLATOR, PXI_CLK10_IN


@pytest.mark.parametrize("source, destination", [(OSCILLATOR, PXI_CLK10_IN)])
def test_signal_and_clock_routing(sync_session, source, destination):
    sync_session.connect_clock_terminals(source, destination)
