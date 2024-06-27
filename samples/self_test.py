"""Module for performing a self-test on an NI-Sync device.

This module provides functionality to perform a self-test on an NI-Sync device using the nisync
library.
"""

from nisync import Session

# Replace 'PXI1Slot10' with the actual resource name of your NI-Sync device.
RESOURCE_NAME = "PXI1Slot10"


def self_test(resource_name):
    """Perform a self-test on the specified NI-Sync device.

    Args:
        resource_name (str): The resource name of the NI-Sync device to test.
    """
    with Session(resource_name=resource_name, reset_device=True) as session:
        test_result, test_message = session.self_test()

        if test_result == 0:
            print("Self-test passed.")
        else:
            print(f"Self-test failed with message: {test_message}")


if __name__ == "__main__":
    self_test(RESOURCE_NAME)
