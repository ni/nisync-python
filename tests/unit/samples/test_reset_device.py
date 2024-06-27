from samples.reset_device import reset_device


def test_reset_device(mocker, capfd):
    mock_session = mocker.patch("samples.reset_device.Session")
    mock_session.return_value.__enter__.return_value.reset.return_value = None

    reset_device("PXI1Slot10")

    mock_session.assert_called_once_with(resource_name="PXI1Slot10")
    mock_session.return_value.__enter__.return_value.reset.assert_called_once()
    stdout, stderr = capfd.readouterr()
    assert "Device has been reset." in stdout
