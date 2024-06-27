from samples.self_test import self_test


def test_self_test_passed(mocker, capfd):
    mock_session = mocker.patch("samples.self_test.Session")
    mock_session.return_value.__enter__.return_value.self_test.return_value = (0, "No error")

    self_test("PXI1Slot10")

    mock_session.assert_called_once_with(resource_name="PXI1Slot10", reset_device=True)
    mock_session.return_value.__enter__.return_value.self_test.assert_called_once()
    stdout, stderr = capfd.readouterr()
    assert "Self-test passed." in stdout


def test_self_test_failed(mocker, capfd):
    mock_session = mocker.patch("samples.self_test.Session")
    mock_session.return_value.__enter__.return_value.self_test.return_value = (-1, "Error")

    self_test("PXI1Slot10")

    mock_session.assert_called_once_with(resource_name="PXI1Slot10", reset_device=True)
    mock_session.return_value.__enter__.return_value.self_test.assert_called_once()
    stdout, stderr = capfd.readouterr()
    assert "Self-test failed with message: Error" in stdout
