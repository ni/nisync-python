def test___self_test___check_returned_error(sync_session_with_reset):
    result, message = sync_session_with_reset.self_test()
    assert result == 0
    assert message == "Self test passed"
