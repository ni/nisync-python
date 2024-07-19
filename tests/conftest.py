"""Configure pytest for testing with nisync devices.

This module includes fixtures for setting up session-wide resources 
and command line options for specifying resource names.It also 
ensures the nisync library singleton is reset before each test to 
avoid side effects.
"""

import pytest

import nisync._library_singleton
from nisync import Session


def pytest_addoption(parser):
    """Add command-line option for specifying the resource name."""
    parser.addoption(
        "--resource_name",
        action="store",
        default="",
        help="pytest includes functional test folder if resource_name is not empty",
    )


def pytest_collection_modifyitems(config, items):
    """Skip functional tests if --resource_name command argurment is not provided."""
    if not config.getoption("--resource_name"):
        skip_special = pytest.mark.skip(
            reason="Require command argurment --resource_name option to run"
        )
        for item in items:
            if "functional_test" in str(item.fspath):  # Adjust the path as needed
                item.add_marker(skip_special)


@pytest.fixture(scope="session")
def resource_name(request):
    """Provide the resource name specified by the command-line option."""
    if request.config.getoption("--resource_name") == "":
        raise ValueError(
            "resource_name cannot be emptied : Use --resource_name=<resource_name> as command line argument"
        )
    return request.config.getoption("--resource_name")


def pytest_configure(config):
    """Reset the nisync library singleton before each test session."""
    nisync._library_singleton._instance = None
    pass


def pytest_runtest_setup(item):
    """Reset the nisync library singleton before each next test session."""
    nisync._library_singleton._instance = None
    pass


@pytest.fixture(scope="function")
def sync_session_with_reset(resource_name):
    """Open a session with reset_device=True and close it after the test."""
    with Session(resource_name, True) as session:
        yield session
    session.close()


@pytest.fixture(scope="function")
def get_sync_session(resource_name):
    """Open a session with reset_device=False and close it after the test."""
    with Session(resource_name, False) as session:
        yield session
    session.close()
