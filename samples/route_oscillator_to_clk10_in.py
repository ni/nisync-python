"""Route the Oscillator to PXI_CLK10_IN terminal on an NI-Sync device.

This script demonstrates how to use the nisync library to route the internal oscillator signal
of an NI-Sync device to the PXI_CLK10_IN terminal of the chassis.
"""

from nisync import Session
from nisync.constants import PXI_CLK10_IN, OSCILLATOR

# Replace 'PXI1Slot10' with the actual resource name of your NI-Sync device.
RESOURCE_NAME = "PXI1Slot10"


def route_oscillator_to_clk10_in(resource_name):
    """Route the oscillator to CLK10_IN on the specified NI-Sync device.

    Args:
        resource_name (str): The resource name of the NI-Sync device.
    """
    with Session(resource_name=resource_name) as session:
        session.connect_clock_terminals(source=OSCILLATOR, destination=PXI_CLK10_IN)
        print("Oscillator is routed to PXI_CLK10_IN.")


if __name__ == "__main__":
    route_oscillator_to_clk10_in(RESOURCE_NAME)
