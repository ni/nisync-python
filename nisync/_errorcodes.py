# This file was generated

from nisync.enums import CtypesEnum


class Status(CtypesEnum):

    #: This device is not properly calibrated.
    #:
    #: #define NISYNC_ERROR_CAL_UNCALIBRATED = NISYNC_WARN_BASE + 60
    #:
    #: nisyncerr_calUncalibrated = 1073365052
    UNCALIBRATED = 1073365052

    #: The request has been accepted by the remote device but processing has not been completed. Wait and attempt to query the property again.
    #:
    #: #define NISYNC_ERROR_NETWORK_CLIENT_IN_PROGRESS = NISYNC_WARN_BASE + 100
    #:
    #: nisyncerr_networkClientInProgress = 1073365092
    NETWORK_CLIENT_IN_PROGRESS = 1073365092

    #: The status code passed to the operation could not be interpreted.
    #:
    #: #define NISYNC_ERROR_UNKNOWN_STATUS = VI_WARN_UNKNOWN_STATUS
    #:
    #: nisyncerr_unknownStatus = 1073676421
    UNKNOWN_STATUS = 1073676421

    #: The specified instrument descriptor is invalid.
    #:
    #: #define NISYNC_ERROR_INVALID_DESCRIPTOR = NISYNC_ERROR_BASE + 1
    #:
    #: nisyncerr_invalidDescriptor = -1074118655
    DESCRIPTOR_INVALID = -1074118655

    #: The mode for this operation is invalid.
    #:
    #: #define NISYNC_ERROR_INVALID_MODE = NISYNC_ERROR_BASE + 2
    #:
    #: nisyncerr_invalidMode = -1074118654
    MODE_INVALID = -1074118654

    #: This operation requires a feature that is not supported.
    #:
    #: #define NISYNC_ERROR_FEATURE_NOT_SUPPORTED = NISYNC_ERROR_BASE + 3
    #:
    #: nisyncerr_featureNotSupported = -1074118653
    FEATURE_NOT_SUPPORTED = -1074118653

    #: There is a version mismatch.
    #:
    #: #define NISYNC_ERROR_VERSION_MISMATCH = NISYNC_ERROR_BASE + 4
    #:
    #: nisyncerr_versionMismatch = -1074118652
    VERSION_MISMATCH = -1074118652

    #: An internal software error occurred.
    #:
    #: #define NISYNC_ERROR_INTERNAL_SOFTWARE = NISYNC_ERROR_BASE + 5
    #:
    #: nisyncerr_internalSoftware = -1074118651
    INTERNAL_SOFTWARE = -1074118651

    #: An error occurred while reading or writing a file.
    #:
    #: #define NISYNC_ERROR_FILE_IO = NISYNC_ERROR_BASE + 6
    #:
    #: nisyncerr_fileIo = -1074118650
    FILE_IO = -1074118650

    #: This device does not support Reset.
    #:
    #: #define NISYNC_ERROR_RESET_NOT_SUPPORTED = NISYNC_ERROR_BASE + 7
    #:
    #: nisyncerr_resetNotSupported = -1074118649
    RESET_NOT_SUPPORTED = -1074118649

    #: A parameter for this operation is of an invalid type.
    #:
    #: #define NISYNC_ERROR_INVALID_TYPE = NISYNC_ERROR_BASE + 8
    #:
    #: nisyncerr_invalidType = -1074118648
    TYPE_INVALID = -1074118648

    #: The NI-Sync API Support is unable to communicate with the NI-Sync Runtime. To resolve this issue, install NI-Sync 18.0 or later.
    #:
    #: #define NISYNC_ERROR_API_SUPPORT_INCOMPATIBLE_WITH_RUNTIME = NISYNC_ERROR_BASE + 9
    #:
    #: nisyncerr_apiSupportIncompatibleWithRuntime = -1074118647
    API_SUPPORT_INCOMPATIBLE_WITH_RUNTIME = -1074118647

    #: An error occurred while initializing the driver.
    #:
    #: #define NISYNC_ERROR_DRIVER_INITIALIZATION = NISYNC_ERROR_BASE + 10
    #:
    #: nisyncerr_driverInitialization = -1074118646
    DRIVER_INITIALIZATION = -1074118646

    #: The driver timed out while performing an operation.
    #:
    #: #define NISYNC_ERROR_DRIVER_TIMEOUT = NISYNC_ERROR_BASE + 11
    #:
    #: nisyncerr_driverTimeout = -1074118645
    DRIVER_TIMEOUT = -1074118645

    #: A failure occurred while reading from the device.
    #:
    #: #define NISYNC_ERROR_READ_FAILURE = NISYNC_ERROR_BASE + 20
    #:
    #: nisyncerr_readFailure = -1074118636
    READ_FAILED = -1074118636

    #: A failure occurred while writing to the device.
    #:
    #: #define NISYNC_ERROR_WRITE_FAILURE = NISYNC_ERROR_BASE + 21
    #:
    #: nisyncerr_writeFailure = -1074118635
    WRITE_FAILED = -1074118635

    #: The specified device was not found.
    #:
    #: #define NISYNC_ERROR_DEVICE_NOT_FOUND = NISYNC_ERROR_BASE + 22
    #:
    #: nisyncerr_deviceNotFound = -1074118634
    DEVICE_NOT_FOUND = -1074118634

    #: The specified device is not ready.
    #:
    #: #define NISYNC_ERROR_DEVICE_NOT_READY = NISYNC_ERROR_BASE + 23
    #:
    #: nisyncerr_deviceNotReady = -1074118633
    DEVICE_NOT_READY = -1074118633

    #: An internal hardware error occurred.
    #:
    #: #define NISYNC_ERROR_INTERNAL_HARDWARE = NISYNC_ERROR_BASE + 24
    #:
    #: nisyncerr_internalHardware = -1074118632
    INTERNAL_HARDWARE = -1074118632

    #: An overflow condition occurred.
    #:
    #: #define NISYNC_ERROR_OVERFLOW = NISYNC_ERROR_BASE + 25
    #:
    #: nisyncerr_overflow = -1074118631
    OVERFLOW = -1074118631

    #: The specified device is a remote device.  Remote devices are not allowed.
    #:
    #: #define NISYNC_ERROR_REMOTE_DEVICE = NISYNC_ERROR_BASE + 26
    #:
    #: nisyncerr_remoteDevice = -1074118630
    REMOTE_DEVICE = -1074118630

    #: The firmware failed to load.
    #:
    #: #define NISYNC_ERROR_FIRMWARE_LOAD = NISYNC_ERROR_BASE + 30
    #:
    #: nisyncerr_firmwareLoad = -1074118626
    FIRMWARE_LOAD = -1074118626

    #: The device is not initialized.
    #:
    #: #define NISYNC_ERROR_DEVICE_NOT_INITIALIZED = NISYNC_ERROR_BASE + 31
    #:
    #: nisyncerr_deviceNotInitialized = -1074118625
    DEVICE_NOT_INITIALIZED = -1074118625

    #: PXI_Clk10 is not present.
    #:
    #: #define NISYNC_ERROR_CLK10_NOT_PRESENT = NISYNC_ERROR_BASE + 32
    #:
    #: nisyncerr_clk10NotPresent = -1074118624
    CLK10_NOT_PRESENT = -1074118624

    #: This device does not support a PLL.
    #:
    #: #define NISYNC_ERROR_PLL_NOT_PRESENT = NISYNC_ERROR_BASE + 40
    #:
    #: nisyncerr_pllNotPresent = -1074118616
    PLL_NOT_PRESENT = -1074118616

    #: The device does not support a DDS.
    #:
    #: #define NISYNC_ERROR_DDS_NOT_PRESENT = NISYNC_ERROR_BASE + 41
    #:
    #: nisyncerr_ddsNotPresent = -1074118615
    DDS_NOT_PRESENT = -1074118615

    #: The specified attribute cannot be set because the DDS is already running.
    #:
    #: #define NISYNC_ERROR_DDS_ALREADY_STARTED = NISYNC_ERROR_BASE + 42
    #:
    #: nisyncerr_ddsAlreadyStarted = -1074118614
    DDS_ALREADY_STARTED = -1074118614

    #: The current DDS frequency is incompatible as a synchronization clock, either the DDS is off or running too fast.
    #:
    #: #define NISYNC_ERROR_DDS_SYNC_CLK_COMBO_INVALID = NISYNC_ERROR_BASE + 43
    #:
    #: nisyncerr_ddsSyncClkComboInvalid = -1074118613
    DDS_SYNC_CLOCK_COMBO_INVALID = -1074118613

    #: The specified source terminal is invalid for this operation.
    #:
    #: #define NISYNC_ERROR_SRC_TERMINAL_INVALID = NISYNC_ERROR_BASE + 50
    #:
    #: nisyncerr_srcTerminalInvalid = -1074118606
    SOURCE_TERMINAL_INVALID = -1074118606

    #: The specified destination terminal is invalid for this operation.
    #:
    #: #define NISYNC_ERROR_DEST_TERMINAL_INVALID = NISYNC_ERROR_BASE + 51
    #:
    #: nisyncerr_destTerminalInvalid = -1074118605
    DESTINATION_TERMINAL_INVALID = -1074118605

    #: The specified terminal is not connected.
    #:
    #: #define NISYNC_ERROR_TERMINAL_NOT_CONNECTED = NISYNC_ERROR_BASE + 52
    #:
    #: nisyncerr_terminalNotConnected = -1074118604
    TERMINAL_NOT_CONNECTED = -1074118604

    #: The specified synchronization clock is invalid for this operation.
    #:
    #: #define NISYNC_ERROR_SYNC_CLK_INVALID = NISYNC_ERROR_BASE + 53
    #:
    #: nisyncerr_syncClkInvalid = -1074118603
    SYNC_CLOCK_INVALID = -1074118603

    #: Terminal for the device is invalid.
    #:
    #: #define NISYNC_ERROR_TERMINAL_INVALID = NISYNC_ERROR_BASE + 54
    #:
    #: nisyncerr_terminalInvalid = -1074118602
    TERMINAL_INVALID = -1074118602

    #: Route failed because the PXI chassis is not identified. The existence of the source terminal depends on the chassis being identified. Use the Measurements & Automation Explorer (MAX) to identify your chassis.
    #:
    #: #define NISYNC_ERROR_SRC_TERMINAL_PXI_CHASSIS_NOT_IDENTIFIED = NISYNC_ERROR_BASE + 55
    #:
    #: nisyncerr_srcTerminalPxiChassisNotIdentified = -1074118601
    SOURCE_TERMINAL_PXI_CHASSIS_NOT_IDENTIFIED = -1074118601

    #: Route failed because the PXI chassis is not identified. The existence of the destination terminal depends on the chassis being identified. Use the Measurements & Automation Explorer (MAX) to identify your chassis.
    #:
    #: #define NISYNC_ERROR_DEST_TERMINAL_PXI_CHASSIS_NOT_IDENTIFIED = NISYNC_ERROR_BASE + 56
    #:
    #: nisyncerr_destTerminalPxiChassisNotIdentified = -1074118600
    DESTINATION_TERMINAL_PXI_CHASSIS_NOT_IDENTIFIED = -1074118600

    #: PXI_Star<n> is available as a source terminal only for devices in a system timing slot. To use PXI_Star<n>, move your device to a system timing slot.
    #:
    #: #define NISYNC_ERROR_SRC_TERMINAL_PXI_STARX_NOT_IN_SYS_TIMING_SLOT = NISYNC_ERROR_BASE + 57
    #:
    #: nisyncerr_srcTerminalPxiStarxNotInSysTimingSlot = -1074118599
    SOURCE_TERMINAL_PXI_STARX_NOT_IN_SYS_TIMING_SLOT = -1074118599

    #: PXI_Star<n> is available as a destination terminal only for devices in a system timing slot. To use PXI_Star<n>, move your device to a system timing slot.
    #:
    #: #define NISYNC_ERROR_DEST_TERMINAL_PXI_STARX_NOT_IN_SYS_TIMING_SLOT = NISYNC_ERROR_BASE + 58
    #:
    #: nisyncerr_destTerminalPxiStarxNotInSysTimingSlot = -1074118598
    DESTINATION_TERMINAL_PXI_STARX_NOT_IN_SYS_TIMING_SLOT = -1074118598

    #: PXI_Clk10_In is available as a destination terminal only for devices in a system timing slot. Move your device to a system timing slot.
    #:
    #: #define NISYNC_ERROR_DEST_TERMINAL_PXI_CLK10_IN_NOT_IN_SYS_TIMING_SLOT = NISYNC_ERROR_BASE + 59
    #:
    #: nisyncerr_destTerminalPxiClk10InNotInSysTimingSlot = -1074118597
    DESTINATION_TERMINAL_PXI_CLK10_IN_NOT_IN_SYS_TIMING_SLOT = -1074118597

    #: The supplied external calibration password is incorrect.
    #:
    #: #define NISYNC_ERROR_CAL_INCORRECT_PASSWORD = NISYNC_ERROR_BASE + 60
    #:
    #: nisyncerr_calIncorrectPassword = -1074118596
    INCORRECT_PASSWORD = -1074118596

    #: The external calibration password contains too many characters.
    #:
    #: #define NISYNC_ERROR_CAL_PASSWORD_TOO_LARGE = NISYNC_ERROR_BASE + 61
    #:
    #: nisyncerr_calPasswordTooLarge = -1074118595
    PASSWORD_TOO_LARGE = -1074118595

    #: The specified calibration operation is not permitted on this session type.
    #:
    #: #define NISYNC_ERROR_CAL_NOT_PERMITTED = NISYNC_ERROR_BASE + 62
    #:
    #: nisyncerr_calNotPermitted = -1074118594
    NOT_PERMITTED = -1074118594

    #: A resource necessary to complete the specified operation is not available; therefore, the operation cannot be completed.
    #:
    #: #define NISYNC_ERROR_RSRC_UNAVAILABLE = NISYNC_ERROR_BASE + 70
    #:
    #: nisyncerr_rsrcUnavailable = -1074118586
    RESOURCE_UNAVAILABLE = -1074118586

    #: A resource necessary to complete the specified operation is already reserved by a previous operation and cannot be shared; therefore, the operation cannot be completed.
    #:
    #: #define NISYNC_ERROR_RSRC_RESERVED = NISYNC_ERROR_BASE + 71
    #:
    #: nisyncerr_rsrcReserved = -1074118585
    RESOURCE_RESERVED = -1074118585

    #: A resource necessary to complete the specified operation is not reserved and should have already been; therefore, the operation cannot be completed
    #:
    #: #define NISYNC_ERROR_RSRC_NOT_RESERVED = NISYNC_ERROR_BASE + 72
    #:
    #: nisyncerr_rsrcNotReserved = -1074118584
    RESOURCE_NOT_RESERVED = -1074118584

    #: A hardware buffer necessary to complete the specified operation is unexpectedly full; therefore, the operation cannot be completed.
    #:
    #: #define NISYNC_ERROR_HW_BUFFER_FULL = NISYNC_ERROR_BASE + 73
    #:
    #: nisyncerr_hwBufferFull = -1074118583
    HARDWARE_BUFFER_FULL = -1074118583

    #: A software buffer necessary to complete the specified operation is unexpectedly full; therefore, the operation cannot be completed.
    #:
    #: #define NISYNC_ERROR_SW_BUFFER_FULL = NISYNC_ERROR_BASE + 74
    #:
    #: nisyncerr_swBufferFull = -1074118582
    SOFTWARE_BUFFER_FULL = -1074118582

    #: A network socket necessary to complete the specified operation has generated a failure; therefore, the operation cannot be completed.
    #:
    #: #define NISYNC_ERROR_SOCKET_FAILURE = NISYNC_ERROR_BASE + 75
    #:
    #: nisyncerr_socketFailure = -1074118581
    SOCKET_FAILED = -1074118581

    #: The specified operation cannot be performed because a session has been aborted or a device has been removed from the system. Handle this situation as required by the application and then, if appropriate, attempt to perform the operation again.
    #:
    #: #define NISYNC_ERROR_SESSION_ABORTED = NISYNC_ERROR_BASE + 76
    #:
    #: nisyncerr_sessionAborted = -1074118580
    SESSION_ABORTED = -1074118580

    #: The specified operation cannot be performed because a session is in the process of being aborted or a device is in the process of being removed from the system. Wait until the abort operation is complete, and attempt to perform the operation again.
    #:
    #: #define NISYNC_ERROR_SESSION_ABORTING = NISYNC_ERROR_BASE + 77
    #:
    #: nisyncerr_sessionAborting = -1074118579
    SESSION_ABORTING = -1074118579

    #: The specified operation cannot be performed since the Active Item was not specified.
    #:
    #: #define NISYNC_ERROR_TERMINAL_NOT_SPECIFIED = NISYNC_ERROR_BASE + 78
    #:
    #: nisyncerr_terminalNotSpecified = -1074118578
    TERMINAL_NOT_SPECIFIED = -1074118578

    #: A 1588 time value has overflowed.  The resulting value is not accurate.
    #:
    #: #define NISYNC_ERROR_TIME_OVERFLOW = NISYNC_ERROR_BASE + 80
    #:
    #: nisyncerr_timeOverflow = -1074118576
    TIME_OVERFLOW = -1074118576

    #: The specified time value is too early to be represented as a 1588 time value.
    #:
    #: #define NISYNC_ERROR_TIME_TOO_EARLY = NISYNC_ERROR_BASE + 81
    #:
    #: nisyncerr_timeTooEarly = -1074118575
    TIME_TOO_EARLY = -1074118575

    #: The specified time value is too late to be represetned as a 1588 time value.
    #:
    #: #define NISYNC_ERROR_TIME_TOO_LATE = NISYNC_ERROR_BASE + 82
    #:
    #: nisyncerr_timeTooLate = -1074118574
    TIME_TOO_LATE = -1074118574

    #: The Precision Time Protocol (PTP) has already been started on this device; therefore, it cannot be started again.
    #:
    #: #define NISYNC_ERROR_PTP_ALREADY_STARTED = NISYNC_ERROR_BASE + 83
    #:
    #: nisyncerr_ptpAlreadyStarted = -1074118573
    PTP_ALREADY_STARTED = -1074118573

    #: The Precision Time Protocol (PTP) has not been started on this device; therefore, it cannot be stopped.
    #:
    #: #define NISYNC_ERROR_PTP_NOT_STARTED = NISYNC_ERROR_BASE + 84
    #:
    #: nisyncerr_ptpNotStarted = -1074118572
    PTP_NOT_STARTED = -1074118572

    #: The specified attribute cannot be set when the Precision Time Protocol (PTP) is in its current state.
    #:
    #: #define NISYNC_ERROR_INVALID_CLOCK_STATE = NISYNC_ERROR_BASE + 85
    #:
    #: nisyncerr_invalidClockState = -1074118571
    CLOCK_STATE_INVALID = -1074118571

    #: The IP address for the specified device cannot be determined; therefore, the specified operation cannot be completed.
    #:
    #: #define NISYNC_ERROR_IP_ADDRESS = NISYNC_ERROR_BASE + 86
    #:
    #: nisyncerr_ipAddress = -1074118570
    IP_ADDRESS = -1074118570

    #: The time for the specified future time event is too soon, or may be in the past, and cannot be programmed in the device before it would occur.
    #:
    #: #define NISYNC_ERROR_FUTURE_TIME_EVENT_TOO_SOON = NISYNC_ERROR_BASE + 87
    #:
    #: nisyncerr_futureTimeEventTooSoon = -1074118569
    FUTURE_TIME_EVENT_TOO_SOON = -1074118569

    #: A clock with the specified period is too short to be generated by the device.
    #:
    #: #define NISYNC_ERROR_CLOCK_PERIOD_TOO_SHORT = NISYNC_ERROR_BASE + 88
    #:
    #: nisyncerr_clockPeriodTooShort = -1074118568
    CLOCK_PERIOD_TOO_SHORT = -1074118568

    #: A future time event with the same time and same terminal as the specified future time event has already been created.  Multiple future time events on the same terminal at the same time cannot be created.
    #:
    #: #define NISYNC_ERROR_DUP_FUTURE_TIME_EVENT = NISYNC_ERROR_BASE + 89
    #:
    #: nisyncerr_dupFutureTimeEvent = -1074118567
    DUPLICATE_FUTURE_TIME_EVENT = -1074118567

    #: The specified sync interval for this 1588 clock is different than the sync interval specified for other 1588 clocks participating in the PTP.  Adjust the sync interval on this 1588 clock or the other 1588 clocks participating in the PTP to the same value.
    #:
    #: #define NISYNC_ERROR_SYNC_INTERVAL_MISMACH = NISYNC_ERROR_BASE + 90
    #:
    #: nisyncerr_syncIntervalMismach = -1074118566
    SYNC_INTERVAL_MISMACH = -1074118566

    #: The specified initial time is invalid.  Initial times must be after 0 hours 1 January 2000 and before 0 hours 1 January 2100.
    #:
    #: #define NISYNC_ERROR_INVALID_INITIAL_TIME = NISYNC_ERROR_BASE + 91
    #:
    #: nisyncerr_invalidInitialTime = -1074118565
    INITIAL_TIME_INVALID = -1074118565

    #: The specified 1588 clock adjustment offset is too large.  The clock adjustment cannot be more than +1 seconds or less than -1 seconds.
    #:
    #: #define NISYNC_ERROR_CLK_ADJ_TOO_LARGE = NISYNC_ERROR_BASE + 92
    #:
    #: nisyncerr_clkAdjTooLarge = -1074118564
    CLOCK_ADJUSTMENT_TOO_LARGE = -1074118564

    #: A clock with the specified period is too large to be generated by the device.
    #:
    #: #define NISYNC_ERROR_CLOCK_PERIOD_TOO_LARGE = NISYNC_ERROR_BASE + 93
    #:
    #: nisyncerr_clockPeriodTooLarge = -1074118563
    CLOCK_PERIOD_TOO_LARGE = -1074118563

    #: The network interface associated with the device was not found.  Ensure that the associated NIC (network interface controller) is installed and enabled.
    #:
    #: #define NISYNC_ERROR_NETWORK_ADAPTER_NOT_FOUND = NISYNC_ERROR_BASE + 94
    #:
    #: nisyncerr_networkAdapterNotFound = -1074118562
    NETWORK_ADAPTER_NOT_FOUND = -1074118562

    #: There are no shared trigger lines between the two devices which are acceptable to both devices. Consider routing the signal through the I/O connectors of the two devices, if applicable.
    #:
    #: #define NISYNC_ERROR_NO_COMMON_TRIG_LINE_FOR_ROUTE = NISYNC_ERROR_BASE + 95
    #:
    #: nisyncerr_noCommonTrigLineForRoute = -1074118561
    NO_COMMON_TRIGGER_LINE_FOR_ROUTE = -1074118561

    #: This device does not support timestamp decimation.
    #:
    #: #define NISYNC_ERROR_TIMESTAMP_DECIMATION_NOT_SUPPORTED = NISYNC_ERROR_BASE + 96
    #:
    #: nisyncerr_timestampDecimationNotSupported = -1074118560
    TIMESTAMP_DECIMATION_NOT_SUPPORTED = -1074118560

    #: The timestamp decimation count must be greater than 0 for this device.
    #:
    #: #define NISYNC_ERROR_TIMESTAMP_DECIMATION_COUNT_TOO_SMALL = NISYNC_ERROR_BASE + 97
    #:
    #: nisyncerr_timestampDecimationCountTooSmall = -1074118559
    TIMESTAMP_DECIMATION_COUNT_TOO_SMALL = -1074118559

    #: The specified timestamp decimation count is too great for this device.
    #:
    #: #define NISYNC_ERROR_TIMESTAMP_DECIMATION_COUNT_TOO_LARGE = NISYNC_ERROR_BASE + 98
    #:
    #: nisyncerr_timestampDecimationCountTooLarge = -1074118558
    TIMESTAMP_DECIMATION_COUNT_TOO_LARGE = -1074118558

    #: The specified future time event violates the rearm time of the future time event engine.
    #:
    #: #define NISYNC_ERROR_FUTURE_TIME_EVENT_REARM_TIME_VIOLATION = NISYNC_ERROR_BASE + 99
    #:
    #: nisyncerr_futureTimeEventRearmTimeViolation = -1074118557
    FUTURE_TIME_EVENT_REARM_TIME_VIOLATION = -1074118557

    #: Board time was snapped back during measurement.
    #:
    #: #define NISYNC_ERROR_TIME_SNAPPED = NISYNC_ERROR_BASE + 100
    #:
    #: nisyncerr_timeSnapped = -1074118556
    TIME_SNAPPED = -1074118556

    #: The requested property is not supported by the time reference specified on the Active Item.
    #:
    #: #define NISYNC_ERROR_TR_TYPE_MISMATCH = NISYNC_ERROR_BASE + 101
    #:
    #: nisyncerr_trTypeMismatch = -1074118555
    TIME_REFERENCE_TYPE_MISMATCH = -1074118555

    #: The requested time reference instance was not found.
    #:
    #: #define NISYNC_ERROR_TR_INSTANCE_NOT_FOUND = NISYNC_ERROR_BASE + 102
    #:
    #: nisyncerr_trInstanceNotFound = -1074118554
    TIME_REFERENCE_INSTANCE_NOT_FOUND = -1074118554

    #: The data received from the remote device could not be interpreted. Try to perform the operation again.
    #:
    #: #define NISYNC_ERROR_REMOTE_DEVICE_READ_FAILURE = NISYNC_ERROR_BASE + 103
    #:
    #: nisyncerr_remoteDeviceReadFailure = -1074118553
    REMOTE_DEVICE_READ_FAILED = -1074118553

    #: A failure occured while communicating with the remote device. Ensure the remote device is accessible.
    #:
    #: #define NISYNC_ERROR_REMOTE_DEVICE_COMMUNICATION_FAILURE = NISYNC_ERROR_BASE + 104
    #:
    #: nisyncerr_remoteDeviceCommunicationFailure = -1074118552
    REMOTE_DEVICE_COMMUNICATION_FAILED = -1074118552

    #: Unable to load an internal library. If the error persists contact NI support.
    #:
    #: #define NISYNC_ERROR_LIB_LOAD_FAILURE = NISYNC_ERROR_BASE + 105
    #:
    #: nisyncerr_libLoadFailure = -1074118551
    LIBRARY_LOAD_FAILED = -1074118551

    #: The resource name format is invalid.
    #:
    #: #define NISYNC_ERROR_INVALID_RESOURCE_NAME_FORMAT = NISYNC_ERROR_BASE + 106
    #:
    #: nisyncerr_invalidResourceNameFormat = -1074118550
    RESOURCE_NAME_FORMAT_INVALID = -1074118550

    #: The specified time reference already exists.
    #:
    #: #define NISYNC_ERROR_TR_INSTANCE_ALREADY_EXISTS = NISYNC_ERROR_BASE + 107
    #:
    #: nisyncerr_trInstanceAlreadyExists = -1074118549
    TIME_REFERENCE_INSTANCE_ALREADY_EXISTS = -1074118549

    #: Requested resource not found on a remote device. This may be because the device was not reachable or has experienced an internal error. It may also mean you need to update software or firmware on the remote device.
    #:
    #: #define NISYNC_ERROR_REMOTE_DEVICE_RESOURCE_NOT_FOUND = NISYNC_ERROR_BASE + 108
    #:
    #: nisyncerr_remoteDeviceResourceNotFound = -1074118548
    REMOTE_DEVICE_RESOURCE_NOT_FOUND = -1074118548

    #: The time reference you are trying to enable conflicts with a time reference already running on the same interface. Disable the conflicting time reference and retry the operation.
    #:
    #: #define NISYNC_ERROR_CONFLICTING_TR_INSTANCES = NISYNC_ERROR_BASE + 109
    #:
    #: nisyncerr_conflictingTrInstances = -1074118547
    CONFLICTING_TIME_REFERENCE_INSTANCES = -1074118547

    #: The requested attribute is not currently available. This may be because the time reference is disabled, not ready, or has encountered an error.
    #:
    #: #define NISYNC_ERROR_TR_ATTR_NOT_FOUND = NISYNC_ERROR_BASE + 110
    #:
    #: nisyncerr_trAttrNotFound = -1074118546
    TIME_REFERENCE_ATTRIBUTE_NOT_FOUND = -1074118546

    #: A failure occured while communicating with a required software service running on the device. Restart the device. If the error persists, contact NI support.
    #:
    #: #define NISYNC_ERROR_COMMUNICATIONS_FAULT = NISYNC_ERROR_BASE + 111
    #:
    #: nisyncerr_communicationsFault = -1074118545
    COMMUNICATIONS_FAILED = -1074118545

    #: The specified attribute is not supported.
    #:
    #: #define NISYNC_ERROR_NSUP_ATTR = VI_ERROR_NSUP_ATTR
    #:
    #: nisyncerr_nsupAttr = -1073807331
    ATTRIBUTE_NOT_SUPPORTED = -1073807331

    #: The specified attribute state is not supported.
    #:
    #: #define NISYNC_ERROR_NSUP_ATTR_STATE = VI_ERROR_NSUP_ATTR_STATE
    #:
    #: nisyncerr_nsupAttrState = -1073807330
    ATTRIBUTE_STATE_NOT_SUPPORTED = -1073807330

    #: The specified attribute is read-only.
    #:
    #: #define NISYNC_ERROR_ATTR_READONLY = VI_ERROR_ATTR_READONLY
    #:
    #: nisyncerr_attrReadonly = -1073807329
    ATTRIBUTE_READONLY = -1073807329

    #: The specified destination terminal is in use.
    #:
    #: #define NISYNC_ERROR_DEST_TERMINAL_IN_USE = VI_ERROR_LINE_IN_USE
    #:
    #: nisyncerr_destTerminalInUse = -1073807294
    DESTINATION_TERMINAL_IN_USE = -1073807294

    #: A parameter for this operation is invalid.
    #:
    #: #define NISYNC_ERROR_INV_PARAMETER = VI_ERROR_INV_PARAMETER
    #:
    #: nisyncerr_invParameter = -1073807240
    PARAMETER_INVALID = -1073807240

    #: Insufficient system resources to perform necessary memory allocation.
    #:
    #: #define NISYNC_ERROR_ALLOC = VI_ERROR_ALLOC
    #:
    #: nisyncerr_allocationFailed = -1073807300
    ALLOCATION_FAILED = -1073807300

    #: The given session or object reference is invalid.
    #:
    #: #define NISYNC_ERROR_INV_OBJECT = VI_ERROR_INV_OBJECT
    #:
    #: nisyncerr_invalidObject = -1073807346
    OBJECT_INVALID = -1073807346

    #: Unknown system error (miscellaneous error).
    #:
    #: #define NISYNC_ERROR_SYSTEM_ERROR = VI_ERROR_SYSTEM_ERROR
    #:
    #: nisyncerr_systemError = -1073807360
    SYSTEM_ERROR = -1073807360
