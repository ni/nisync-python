import pytest

from nisync import Session


@pytest.mark.parametrize("reset_device", [True, False])
def test_session(resource_name, reset_device):
    with Session(resource_name, reset_device) as session:
        session.__enter__()


def test_close_session(resource_name):
    with Session(resource_name, False) as session:
        session.close()
