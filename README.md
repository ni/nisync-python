| Info      | Contains a Python API for interacting with NI-Sync. See [GitHub](https://github.com/ni/nisync-python/) for the latest source. | 
| :-------- | :---------------------| 
| Author    | National Instruments  | 

# Table of Contents
- [About](#about)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Documentation](#documentation)
- [License](#license)

# About

The **nisync** package contains an API (Application Programming Interface)
for interacting with the NI-Sync driver. The package is implemented in Python.
The package is implemented as a complex,
highly object-oriented wrapper around the NI-Sync C API using the
[ctypes](https://docs.python.org/2/library/ctypes.html) Python library.

**nisync** supports all versions of the NI-Sync driver that ships with the C
API. The C API is included in any version of the driver that supports it. The
**nisync** package does not require installation of the C header files.

Some functions in the **nisync** package may be unavailable with earlier
versions of the NI-Sync driver. Visit the
[ni.com/downloads](http://www.ni.com/downloads/) to upgrade your version of
NI-Sync.

**nisync** supports Windows and Linux operating systems where the NI-Sync
driver is supported. Refer to
[NI Hardware and Operating System Compatibility](https://www.ni.com/r/hw-support)
for which versions of the driver support your hardware on a given operating
system.

# Installation

Running **nisync** requires NI-Sync to be installed. Visit
[ni.com/downloads](http://www.ni.com/downloads/) to download the latest
version of NI-Sync. None of the recommended **Additional items** are required
for **nisync** to function, and they can be removed to minimize installation
size. It is recommended you continue to install the **NI Certificates** package
to allow your Operating System to trust NI built binaries, improving your
software and hardware installation experience.

**nisync** can be installed with [pip](http://pypi.python.org/pypi/pip>):

```shell
python -m pip install nisync
```

# Getting Started
In order to use the **nisync** package, you must have at least one device that supports NI-Sync 
installed on your system. Both physical and simulated devices are supported.
You can use **NI MAX** or **NI Hardware Configuration Utility** to verify and configure your devices.

# Usage
The following is a basic example of using an **nisync.nisync.Session** object. This example illustrates how to connect and disconnect clock terminals to synchronize devices using the onboard oscillator as the clock source. This is particularly useful in applications requiring precise timing and synchronization across multiple devices.

```python
import nisync
from nisync.constants import PXI_CLK10_IN, OSCILLATOR

# Create a new session with the nisync library
with nisync.Session(resource_name="PXI1Slot10") as session:
    # Connect the onboard oscillator to the PXI_CLK10_IN terminal
    # This setup is typically used for synchronizing measurements across devices
    session.connect_clock_terminals(OSCILLATOR, PXI_CLK10_IN)
    
    # Perform measurements or operations that require synchronization
    
    # Once operations are complete, disconnect the terminals
    session.disconnect_clock_terminals(OSCILLATOR, PXI_CLK10_IN)
```


# Documentation

Refer to the [NI-Sync Help](https://www.ni.com/docs/en-US/bundle/ni-sync/page/user-manual-welcome.html)
for API-agnostic information about NI-Sync concepts.

# License

**nisync** is licensed under an MIT-style license (see
[LICENSE](https://github.com/ni/nisync-python/blob/main/LICENSE)).
Other incorporated projects may be licensed under different licenses. All
licenses allow for non-commercial and commercial use.
