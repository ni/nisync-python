def test_self_test(sync_session_with_reset):
    result,message = sync_session_with_reset.self_test()
    assert result == 0

def test_close(get_sync_session):
    get_sync_session.close()
