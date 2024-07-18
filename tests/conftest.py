import pytest
from nisync import Session
import nisync._library_singleton

def pytest_addoption(parser):
    parser.addoption("--resource_name", action="store", default="", help="Resource name of the device")

@pytest.fixture(scope="session")
def resource_name(request):
    if(request.config.getoption("--resource_name") == ""):
        raise ValueError("resource_name cannot be emptied : Use --resource_name=<resource_name> as command line argument")
    return request.config.getoption("--resource_name")

def pytest_configure(config):
    # Reset the singleton instance to avoid side effects between tests
    nisync._library_singleton._instance = None
    pass

def pytest_runtest_setup(item):
    nisync._library_singleton._instance = None
    pass

@pytest.fixture(scope="function")
def sync_session_with_reset(resource_name):
    with Session(resource_name, True) as session:
        yield session
    session.close()

@pytest.fixture(scope="function")
def get_sync_session(resource_name):
    with Session(resource_name, False) as session:
        yield session
    session.close()