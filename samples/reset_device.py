"""Module for resetting an NI-Sync device.

This module provides functionality to reset an NI-Sync device using the nisync library.
"""

from nisync import Session

# Replace 'PXI1Slot10' with the actual resource name of your NI-Sync device.
RESOURCE_NAME = "PXI1Slot10"


def reset_device(resource_name):
    """Reset the specified NI-Sync device.

    Args:
        resource_name (str): The resource name of the NI-Sync device to reset.
    """
    with Session(resource_name=resource_name) as session:
        session.reset()
        print("Device has been reset.")


if __name__ == "__main__":
    reset_device(RESOURCE_NAME)
