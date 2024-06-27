from samples.route_oscillator_to_clk10_in import route_oscillator_to_clk10_in

from nisync.constants import CLK10_IN, OSCILLATOR


def test_route_oscillator_to_clk10_in(mocker, capfd):
    mock_session = mocker.patch("samples.route_oscillator_to_clk10_in.Session")
    resource_name = "PXI1Slot2"

    route_oscillator_to_clk10_in(resource_name)

    mock_session.assert_called_once_with(resource_name=resource_name)
    mock_session.return_value.__enter__.return_value.connect_clock_terminals.assert_called_once_with(
        source=OSCILLATOR, destination=CLK10_IN
    )
    mock_session.return_value.__exit__.assert_called()
    stdout, stderr = capfd.readouterr()
    assert "Oscillator is routed to PXI_CLK10_IN." in stdout
