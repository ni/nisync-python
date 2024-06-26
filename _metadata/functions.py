# -*- coding: utf-8 -*-
# This file is code generated, do not make changes here
#  If the generated information is not correct for python
#  changes can be made in functions_addon.py and they will be
#  applied at build time

functions = {
    "init": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "resourceName",
                "type": "ViRsrc",
            },
            {
                "direction": "in",
                "name": "IDQuery",
                "type": "ViBoolean",
            },
            {
                "direction": "in",
                "name": "resetDevice",
                "type": "ViBoolean",
            },
            {
                "direction": "out",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "close": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "GetTimeReferenceNames": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "bufferSize",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timeReferenceNames",
                "type": "ViChar",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "error_message": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "errorCode",
                "type": "ViStatus",
            },
            {
                "direction": "out",
                "name": "errorMessage",
                "type": "ViChar",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "reset": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "PersistConfig": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "self_test": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "selfTestResult",
                "type": "ViInt16",
            },
            {
                "direction": "out",
                "name": "selfTestMessage",
                "type": "ViChar",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "revision_query": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "instrumentDriverRevision",
                "type": "ViChar",
            },
            {
                "direction": "out",
                "name": "firmwareRevision",
                "type": "ViChar",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "ConfigureFPGA": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "fpgaProgramPath",
                "type": "ViConstString",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "ConnectTrigTerminals": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "destTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "syncClock",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "invert",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "updateEdge",
                "type": "ViInt32",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "DisconnectTrigTerminals": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "destTerminal",
                "type": "ViConstString",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "GetTrigTerminalConnectionInfo": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "destTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "out",
                "name": "srcTerminal",
                "type": "ViChar",
            },
            {
                "direction": "out",
                "name": "syncClock",
                "type": "ViChar",
            },
            {
                "direction": "out",
                "name": "invert",
                "type": "ViInt32",
            },
            {
                "direction": "out",
                "name": "updateEdge",
                "type": "ViInt32",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "ConnectSWTrigToTerminal": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "destTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "syncClock",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "invert",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "updateEdge",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "delay",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "DisconnectSWTrigFromTerminal": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "destTerminal",
                "type": "ViConstString",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "GetSWTrigConnectionInfo": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "destTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "out",
                "name": "srcTerminal",
                "type": "ViChar",
            },
            {
                "direction": "out",
                "name": "syncClk",
                "type": "ViChar",
            },
            {
                "direction": "out",
                "name": "invert",
                "type": "ViInt32",
            },
            {
                "direction": "out",
                "name": "updateEdge",
                "type": "ViInt32",
            },
            {
                "direction": "out",
                "name": "delay",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "SendSoftwareTrigger": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "ConnectClkTerminals": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "destTerminal",
                "type": "ViConstString",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "DisconnectClkTerminals": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "destTerminal",
                "type": "ViConstString",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "GetClkTerminalConnectionInfo": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "destTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "out",
                "name": "srcTerminal",
                "type": "ViChar",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "MeasureFrequency": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "duration",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "actualDuration",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "frequency",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "frequencyError",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "MeasureFrequencyEx": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "srcTerminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "duration",
                "type": "ViReal64",
            },
            {
                "direction": "in",
                "name": "decimationCount",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "actualDuration",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "frequency",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "frequencyError",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "Start1588": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "Stop1588": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "SetTime": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "timeSource",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "timeSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "timeNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "timeFractionalNanoseconds",
                "type": "ViUInt16",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "GetTime": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "timeSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timeNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timeFractionalNanoseconds",
                "type": "ViUInt16",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "ResetFrequency": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "CreateFutureTimeEvent": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "outputLevel",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "timeSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "timeNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "timeFractionalNanoseconds",
                "type": "ViUInt16",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "ClearFutureTimeEvents": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "EnableTimeStampTrigger": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "activeEdge",
                "type": "ViInt32",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "EnableTimeStampTriggerWithDecimation": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "activeEdge",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "decimationCount",
                "type": "ViUInt32",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "ReadTriggerTimeStamp": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "timeout",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "timeSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timeNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timeFractionalNanoseconds",
                "type": "ViUInt16",
            },
            {
                "direction": "out",
                "name": "detectedEdge",
                "type": "ViInt32",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "ReadMultipleTriggerTimeStamp": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "timestampsToRead",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "timeout",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "timeSecondsBuffer",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timeNanosecondsBuffer",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timeFractionalNanosecondsBuffer",
                "type": "ViUInt16",
            },
            {
                "direction": "out",
                "name": "detectedEdgeBuffer",
                "type": "ViInt32",
            },
            {
                "direction": "out",
                "name": "timestampsRead",
                "type": "ViUInt32",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "DisableTimeStampTrigger": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "CreateClock": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "highTicks",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "lowTicks",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "startTimeSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "startTimeNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "startTimeFractionalNanoseconds",
                "type": "ViUInt16",
            },
            {
                "direction": "in",
                "name": "stopTimeSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "stopTimeNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "stopTimeFractionalNanoseconds",
                "type": "ViUInt16",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "ClearClock": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "Start8021AS": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "Stop8021AS": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "SetTimeReferenceFreeRunning": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "SetTimeReferenceGPS": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "SetTimeReferenceIRIG": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "irigType",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "terminalName",
                "type": "ViConstString",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "SetTimeReferencePPS": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminalName",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "useManualTime",
                "type": "ViBoolean",
            },
            {
                "direction": "in",
                "name": "initialTimeSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "initialTimeNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "initialTimeFractionalNanoseconds",
                "type": "ViUInt16",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "SetTimeReference1588OrdinaryClock": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "SetTimeReference8021AS": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "EnableGPSTimestamping": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "EnableIRIGTimestamping": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "irigType",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "terminalName",
                "type": "ViConstString",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "ReadLastGPSTimestamp": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "timestampSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timestampNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timestampFractionalNanoseconds",
                "type": "ViUInt16",
            },
            {
                "direction": "out",
                "name": "gpsSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "gpsNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "gpsFractionalNanoseconds",
                "type": "ViUInt16",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "ReadLastIRIGTimestamp": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminal",
                "type": "ViConstString",
            },
            {
                "direction": "out",
                "name": "timestampSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timestampNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timestampFractionalNanoseconds",
                "type": "ViUInt16",
            },
            {
                "direction": "out",
                "name": "irigbSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "irigbNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "irigbFractionalNanoseconds",
                "type": "ViUInt16",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "DisableGPSTimestamping": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "DisableIRIGTimestamping": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "terminalName",
                "type": "ViConstString",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "GetVelocity": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "eastVelocity",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "northVelocity",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "upVelocity",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "GetLocation": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "latitude",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "longitude",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "altitude",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "GetAttributeViInt32": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "activeItem",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "attribute",
                "type": "ViAttr",
            },
            {
                "direction": "out",
                "name": "value",
                "type": "ViInt32",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "GetAttributeViReal64": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "activeItem",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "attribute",
                "type": "ViAttr",
            },
            {
                "direction": "out",
                "name": "value",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "GetAttributeViBoolean": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "activeItem",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "attribute",
                "type": "ViAttr",
            },
            {
                "direction": "out",
                "name": "value",
                "type": "ViBoolean",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "GetAttributeViString": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "activeItem",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "attribute",
                "type": "ViAttr",
            },
            {
                "direction": "in",
                "name": "bufferSize",
                "type": "ViInt32",
            },
            {
                "direction": "out",
                "name": "value",
                "type": "ViChar",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "SetAttributeViInt32": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "activeItem",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "attribute",
                "type": "ViAttr",
            },
            {
                "direction": "in",
                "name": "value",
                "type": "ViInt32",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "SetAttributeViReal64": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "activeItem",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "attribute",
                "type": "ViAttr",
            },
            {
                "direction": "in",
                "name": "value",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "SetAttributeViBoolean": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "activeItem",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "attribute",
                "type": "ViAttr",
            },
            {
                "direction": "in",
                "name": "value",
                "type": "ViBoolean",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "SetAttributeViString": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "activeItem",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "attribute",
                "type": "ViAttr",
            },
            {
                "direction": "in",
                "name": "value",
                "type": "ViConstString",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "GetExtCalLastDateAndTime": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "year",
                "type": "ViInt32",
            },
            {
                "direction": "out",
                "name": "month",
                "type": "ViInt32",
            },
            {
                "direction": "out",
                "name": "day",
                "type": "ViInt32",
            },
            {
                "direction": "out",
                "name": "hour",
                "type": "ViInt32",
            },
            {
                "direction": "out",
                "name": "minute",
                "type": "ViInt32",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "GetExtCalLastTemp": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "temp",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "GetExtCalRecommendedInterval": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "months",
                "type": "ViInt32",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "ChangeExtCalPassword": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "oldPassword",
                "type": "ViConstString",
            },
            {
                "direction": "in",
                "name": "newPassword",
                "type": "ViConstString",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "ReadCurrentTemperature": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "temperature",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "CalGetOscillatorVoltage": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "voltage",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "CalGetClk10PhaseVoltage": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "voltage",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "CalGetDDSStartPulsePhaseVoltage": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "voltage",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "CalGetDDSInitialPhase": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "phase",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "InitExtCal": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "resourceName",
                "type": "ViRsrc",
            },
            {
                "direction": "in",
                "name": "password",
                "type": "ViConstString",
            },
            {
                "direction": "out",
                "name": "extCalVi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "CloseExtCal": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "extCalVi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "action",
                "type": "ViInt32",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "CalAdjustOscillatorVoltage": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "extCalVi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "measuredVoltage",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "oldVoltage",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "CalAdjustClk10PhaseVoltage": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "extCalVi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "measuredVoltage",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "oldVoltage",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "CalAdjustDDSStartPulsePhaseVoltage": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "extCalVi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "measuredVoltage",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "oldVoltage",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "CalAdjustDDSInitialPhase": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "extCalVi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "measuredPhase",
                "type": "ViReal64",
            },
            {
                "direction": "out",
                "name": "oldPhase",
                "type": "ViReal64",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "StartPTP": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "in",
                "name": "initialTimeSource",
                "type": "ViInt32",
            },
            {
                "direction": "in",
                "name": "initialTimeSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "initialTimeNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "in",
                "name": "initialTimeFractionalNanoseconds",
                "type": "ViUInt16",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "StopPTP": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
    "Get1588Time": {
        "returns": "ViStatus",
        "parameters": [
            {
                "direction": "in",
                "name": "vi",
                "type": "ViSession",
            },
            {
                "direction": "out",
                "name": "timeSeconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timeNanoseconds",
                "type": "ViUInt32",
            },
            {
                "direction": "out",
                "name": "timeFractionalNanoseconds",
                "type": "ViUInt16",
            },
        ],
        "codegen_method": "public",
        "visibility": "public",
    },
}
