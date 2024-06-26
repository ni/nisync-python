# This file was generated

import ctypes
import threading
from nisync._visatype import *  # noqa: F403


def ascii_encode(value):
    if isinstance(value, str):
        return value.encode("ascii")
    return value


class Library(object):
    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niSync_init_cfunc = None
        self.niSync_close_cfunc = None
        self.niSync_GetTimeReferenceNames_cfunc = None
        self.niSync_error_message_cfunc = None
        self.niSync_reset_cfunc = None
        self.niSync_PersistConfig_cfunc = None
        self.niSync_self_test_cfunc = None
        self.niSync_revision_query_cfunc = None
        self.niSync_ConfigureFPGA_cfunc = None
        self.niSync_ConnectTrigTerminals_cfunc = None
        self.niSync_DisconnectTrigTerminals_cfunc = None
        self.niSync_GetTrigTerminalConnectionInfo_cfunc = None
        self.niSync_ConnectSWTrigToTerminal_cfunc = None
        self.niSync_DisconnectSWTrigFromTerminal_cfunc = None
        self.niSync_GetSWTrigConnectionInfo_cfunc = None
        self.niSync_SendSoftwareTrigger_cfunc = None
        self.niSync_ConnectClkTerminals_cfunc = None
        self.niSync_DisconnectClkTerminals_cfunc = None
        self.niSync_GetClkTerminalConnectionInfo_cfunc = None
        self.niSync_MeasureFrequency_cfunc = None
        self.niSync_MeasureFrequencyEx_cfunc = None
        self.niSync_Start1588_cfunc = None
        self.niSync_Stop1588_cfunc = None
        self.niSync_SetTime_cfunc = None
        self.niSync_GetTime_cfunc = None
        self.niSync_ResetFrequency_cfunc = None
        self.niSync_CreateFutureTimeEvent_cfunc = None
        self.niSync_ClearFutureTimeEvents_cfunc = None
        self.niSync_EnableTimeStampTrigger_cfunc = None
        self.niSync_EnableTimeStampTriggerWithDecimation_cfunc = None
        self.niSync_ReadTriggerTimeStamp_cfunc = None
        self.niSync_ReadMultipleTriggerTimeStamp_cfunc = None
        self.niSync_DisableTimeStampTrigger_cfunc = None
        self.niSync_CreateClock_cfunc = None
        self.niSync_ClearClock_cfunc = None
        self.niSync_Start8021AS_cfunc = None
        self.niSync_Stop8021AS_cfunc = None
        self.niSync_SetTimeReferenceFreeRunning_cfunc = None
        self.niSync_SetTimeReferenceGPS_cfunc = None
        self.niSync_SetTimeReferenceIRIG_cfunc = None
        self.niSync_SetTimeReferencePPS_cfunc = None
        self.niSync_SetTimeReference1588OrdinaryClock_cfunc = None
        self.niSync_SetTimeReference8021AS_cfunc = None
        self.niSync_EnableGPSTimestamping_cfunc = None
        self.niSync_EnableIRIGTimestamping_cfunc = None
        self.niSync_ReadLastGPSTimestamp_cfunc = None
        self.niSync_ReadLastIRIGTimestamp_cfunc = None
        self.niSync_DisableGPSTimestamping_cfunc = None
        self.niSync_DisableIRIGTimestamping_cfunc = None
        self.niSync_GetVelocity_cfunc = None
        self.niSync_GetLocation_cfunc = None
        self.niSync_GetAttributeViInt32_cfunc = None
        self.niSync_GetAttributeViReal64_cfunc = None
        self.niSync_GetAttributeViBoolean_cfunc = None
        self.niSync_GetAttributeViString_cfunc = None
        self.niSync_SetAttributeViInt32_cfunc = None
        self.niSync_SetAttributeViReal64_cfunc = None
        self.niSync_SetAttributeViBoolean_cfunc = None
        self.niSync_SetAttributeViString_cfunc = None
        self.niSync_GetExtCalLastDateAndTime_cfunc = None
        self.niSync_GetExtCalLastTemp_cfunc = None
        self.niSync_GetExtCalRecommendedInterval_cfunc = None
        self.niSync_ChangeExtCalPassword_cfunc = None
        self.niSync_ReadCurrentTemperature_cfunc = None
        self.niSync_CalGetOscillatorVoltage_cfunc = None
        self.niSync_CalGetClk10PhaseVoltage_cfunc = None
        self.niSync_CalGetDDSStartPulsePhaseVoltage_cfunc = None
        self.niSync_CalGetDDSInitialPhase_cfunc = None
        self.niSync_InitExtCal_cfunc = None
        self.niSync_CloseExtCal_cfunc = None
        self.niSync_CalAdjustOscillatorVoltage_cfunc = None
        self.niSync_CalAdjustClk10PhaseVoltage_cfunc = None
        self.niSync_CalAdjustDDSStartPulsePhaseVoltage_cfunc = None
        self.niSync_CalAdjustDDSInitialPhase_cfunc = None
        self.niSync_StartPTP_cfunc = None
        self.niSync_StopPTP_cfunc = None
        self.niSync_Get1588Time_cfunc = None

    def niSync_init(self, resourceName, IDQuery, resetDevice, vi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_init_cfunc is None:
                self.niSync_init_cfunc = self._library.niSync_init
                self.niSync_init_cfunc.argtypes = [
                    ViRsrc,
                    ViBoolean,
                    ViBoolean,
                    ctypes.POINTER(ViSession),
                ]  # noqa: F405
                self.niSync_init_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_init_cfunc(ascii_encode(resourceName), IDQuery, resetDevice, vi)

    def niSync_close(self, vi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_close_cfunc is None:
                self.niSync_close_cfunc = self._library.niSync_close
                self.niSync_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_close_cfunc(vi)

    def niSync_GetTimeReferenceNames(self, vi, bufferSize, timeReferenceNames):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_GetTimeReferenceNames_cfunc is None:
                self.niSync_GetTimeReferenceNames_cfunc = self._library.niSync_GetTimeReferenceNames
                self.niSync_GetTimeReferenceNames_cfunc.argtypes = [
                    ViSession,
                    ViUInt32,
                    ctypes.POINTER(ViChar),
                ]  # noqa: F405
                self.niSync_GetTimeReferenceNames_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetTimeReferenceNames_cfunc(vi, bufferSize, timeReferenceNames)

    def niSync_error_message(self, vi, errorCode, errorMessage):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_error_message_cfunc is None:
                self.niSync_error_message_cfunc = self._library.niSync_error_message
                self.niSync_error_message_cfunc.argtypes = [
                    ViSession,
                    ViStatus,
                    ctypes.POINTER(ViChar),
                ]  # noqa: F405
                self.niSync_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_error_message_cfunc(vi, errorCode, errorMessage)

    def niSync_reset(self, vi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_reset_cfunc is None:
                self.niSync_reset_cfunc = self._library.niSync_reset
                self.niSync_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_reset_cfunc(vi)

    def niSync_PersistConfig(self, vi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_PersistConfig_cfunc is None:
                self.niSync_PersistConfig_cfunc = self._library.niSync_PersistConfig
                self.niSync_PersistConfig_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_PersistConfig_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_PersistConfig_cfunc(vi)

    def niSync_self_test(self, vi, selfTestResult, selfTestMessage):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_self_test_cfunc is None:
                self.niSync_self_test_cfunc = self._library.niSync_self_test
                self.niSync_self_test_cfunc.argtypes = [
                    ViSession,
                    ctypes.POINTER(ViInt16),
                    ctypes.POINTER(ViChar),
                ]  # noqa: F405
                self.niSync_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_self_test_cfunc(vi, selfTestResult, selfTestMessage)

    def niSync_revision_query(
        self, vi, instrumentDriverRevision, firmwareRevision
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_revision_query_cfunc is None:
                self.niSync_revision_query_cfunc = self._library.niSync_revision_query
                self.niSync_revision_query_cfunc.argtypes = [
                    ViSession,
                    ctypes.POINTER(ViChar),
                    ctypes.POINTER(ViChar),
                ]  # noqa: F405
                self.niSync_revision_query_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_revision_query_cfunc(vi, instrumentDriverRevision, firmwareRevision)

    def niSync_ConfigureFPGA(self, vi, fpgaProgramPath):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_ConfigureFPGA_cfunc is None:
                self.niSync_ConfigureFPGA_cfunc = self._library.niSync_ConfigureFPGA
                self.niSync_ConfigureFPGA_cfunc.argtypes = [ViSession, ViConstString]  # noqa: F405
                self.niSync_ConfigureFPGA_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ConfigureFPGA_cfunc(vi, ascii_encode(fpgaProgramPath))

    def niSync_ConnectTrigTerminals(
        self, vi, srcTerminal, destTerminal, syncClock, invert, updateEdge
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_ConnectTrigTerminals_cfunc is None:
                self.niSync_ConnectTrigTerminals_cfunc = self._library.niSync_ConnectTrigTerminals
                self.niSync_ConnectTrigTerminals_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViConstString,
                    ViConstString,
                    ViInt32,
                    ViInt32,
                ]  # noqa: F405
                self.niSync_ConnectTrigTerminals_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ConnectTrigTerminals_cfunc(
            vi,
            ascii_encode(srcTerminal),
            ascii_encode(destTerminal),
            ascii_encode(syncClock),
            invert,
            updateEdge,
        )

    def niSync_DisconnectTrigTerminals(self, vi, srcTerminal, destTerminal):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_DisconnectTrigTerminals_cfunc is None:
                self.niSync_DisconnectTrigTerminals_cfunc = (
                    self._library.niSync_DisconnectTrigTerminals
                )
                self.niSync_DisconnectTrigTerminals_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViConstString,
                ]  # noqa: F405
                self.niSync_DisconnectTrigTerminals_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_DisconnectTrigTerminals_cfunc(
            vi, ascii_encode(srcTerminal), ascii_encode(destTerminal)
        )

    def niSync_GetTrigTerminalConnectionInfo(
        self, vi, destTerminal, srcTerminal, syncClock, invert, updateEdge
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_GetTrigTerminalConnectionInfo_cfunc is None:
                self.niSync_GetTrigTerminalConnectionInfo_cfunc = (
                    self._library.niSync_GetTrigTerminalConnectionInfo
                )
                self.niSync_GetTrigTerminalConnectionInfo_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ctypes.POINTER(ViChar),
                    ctypes.POINTER(ViChar),
                    ctypes.POINTER(ViInt32),
                    ctypes.POINTER(ViInt32),
                ]  # noqa: F405
                self.niSync_GetTrigTerminalConnectionInfo_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetTrigTerminalConnectionInfo_cfunc(
            vi, ascii_encode(destTerminal), srcTerminal, syncClock, invert, updateEdge
        )

    def niSync_ConnectSWTrigToTerminal(
        self, vi, srcTerminal, destTerminal, syncClock, invert, updateEdge, delay
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_ConnectSWTrigToTerminal_cfunc is None:
                self.niSync_ConnectSWTrigToTerminal_cfunc = (
                    self._library.niSync_ConnectSWTrigToTerminal
                )
                self.niSync_ConnectSWTrigToTerminal_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViConstString,
                    ViConstString,
                    ViInt32,
                    ViInt32,
                    ViReal64,
                ]  # noqa: F405
                self.niSync_ConnectSWTrigToTerminal_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ConnectSWTrigToTerminal_cfunc(
            vi,
            ascii_encode(srcTerminal),
            ascii_encode(destTerminal),
            ascii_encode(syncClock),
            invert,
            updateEdge,
            delay,
        )

    def niSync_DisconnectSWTrigFromTerminal(self, vi, srcTerminal, destTerminal):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_DisconnectSWTrigFromTerminal_cfunc is None:
                self.niSync_DisconnectSWTrigFromTerminal_cfunc = (
                    self._library.niSync_DisconnectSWTrigFromTerminal
                )
                self.niSync_DisconnectSWTrigFromTerminal_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViConstString,
                ]  # noqa: F405
                self.niSync_DisconnectSWTrigFromTerminal_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_DisconnectSWTrigFromTerminal_cfunc(
            vi, ascii_encode(srcTerminal), ascii_encode(destTerminal)
        )

    def niSync_GetSWTrigConnectionInfo(
        self, vi, destTerminal, srcTerminal, syncClk, invert, updateEdge, delay
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_GetSWTrigConnectionInfo_cfunc is None:
                self.niSync_GetSWTrigConnectionInfo_cfunc = (
                    self._library.niSync_GetSWTrigConnectionInfo
                )
                self.niSync_GetSWTrigConnectionInfo_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ctypes.POINTER(ViChar),
                    ctypes.POINTER(ViChar),
                    ctypes.POINTER(ViInt32),
                    ctypes.POINTER(ViInt32),
                    ctypes.POINTER(ViReal64),
                ]  # noqa: F405
                self.niSync_GetSWTrigConnectionInfo_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetSWTrigConnectionInfo_cfunc(
            vi, ascii_encode(destTerminal), srcTerminal, syncClk, invert, updateEdge, delay
        )

    def niSync_SendSoftwareTrigger(self, vi, srcTerminal):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_SendSoftwareTrigger_cfunc is None:
                self.niSync_SendSoftwareTrigger_cfunc = self._library.niSync_SendSoftwareTrigger
                self.niSync_SendSoftwareTrigger_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                ]  # noqa: F405
                self.niSync_SendSoftwareTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SendSoftwareTrigger_cfunc(vi, ascii_encode(srcTerminal))

    def niSync_ConnectClkTerminals(self, vi, srcTerminal, destTerminal):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_ConnectClkTerminals_cfunc is None:
                self.niSync_ConnectClkTerminals_cfunc = self._library.niSync_ConnectClkTerminals
                self.niSync_ConnectClkTerminals_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViConstString,
                ]  # noqa: F405
                self.niSync_ConnectClkTerminals_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ConnectClkTerminals_cfunc(
            vi, ascii_encode(srcTerminal), ascii_encode(destTerminal)
        )

    def niSync_DisconnectClkTerminals(self, vi, srcTerminal, destTerminal):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_DisconnectClkTerminals_cfunc is None:
                self.niSync_DisconnectClkTerminals_cfunc = (
                    self._library.niSync_DisconnectClkTerminals
                )
                self.niSync_DisconnectClkTerminals_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViConstString,
                ]  # noqa: F405
                self.niSync_DisconnectClkTerminals_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_DisconnectClkTerminals_cfunc(
            vi, ascii_encode(srcTerminal), ascii_encode(destTerminal)
        )

    def niSync_GetClkTerminalConnectionInfo(self, vi, destTerminal, srcTerminal):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_GetClkTerminalConnectionInfo_cfunc is None:
                self.niSync_GetClkTerminalConnectionInfo_cfunc = (
                    self._library.niSync_GetClkTerminalConnectionInfo
                )
                self.niSync_GetClkTerminalConnectionInfo_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ctypes.POINTER(ViChar),
                ]  # noqa: F405
                self.niSync_GetClkTerminalConnectionInfo_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetClkTerminalConnectionInfo_cfunc(
            vi, ascii_encode(destTerminal), srcTerminal
        )

    def niSync_MeasureFrequency(
        self, vi, srcTerminal, duration, actualDuration, frequency, frequencyError
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_MeasureFrequency_cfunc is None:
                self.niSync_MeasureFrequency_cfunc = self._library.niSync_MeasureFrequency
                self.niSync_MeasureFrequency_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViReal64,
                    ctypes.POINTER(ViReal64),
                    ctypes.POINTER(ViReal64),
                    ctypes.POINTER(ViReal64),
                ]  # noqa: F405
                self.niSync_MeasureFrequency_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_MeasureFrequency_cfunc(
            vi, ascii_encode(srcTerminal), duration, actualDuration, frequency, frequencyError
        )

    def niSync_MeasureFrequencyEx(
        self, vi, srcTerminal, duration, decimationCount, actualDuration, frequency, frequencyError
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_MeasureFrequencyEx_cfunc is None:
                self.niSync_MeasureFrequencyEx_cfunc = self._library.niSync_MeasureFrequencyEx
                self.niSync_MeasureFrequencyEx_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViReal64,
                    ViUInt32,
                    ctypes.POINTER(ViReal64),
                    ctypes.POINTER(ViReal64),
                    ctypes.POINTER(ViReal64),
                ]  # noqa: F405
                self.niSync_MeasureFrequencyEx_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_MeasureFrequencyEx_cfunc(
            vi,
            ascii_encode(srcTerminal),
            duration,
            decimationCount,
            actualDuration,
            frequency,
            frequencyError,
        )

    def niSync_Start1588(self, vi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_Start1588_cfunc is None:
                self.niSync_Start1588_cfunc = self._library.niSync_Start1588
                self.niSync_Start1588_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_Start1588_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_Start1588_cfunc(vi)

    def niSync_Stop1588(self, vi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_Stop1588_cfunc is None:
                self.niSync_Stop1588_cfunc = self._library.niSync_Stop1588
                self.niSync_Stop1588_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_Stop1588_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_Stop1588_cfunc(vi)

    def niSync_SetTime(
        self, vi, timeSource, timeSeconds, timeNanoseconds, timeFractionalNanoseconds
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_SetTime_cfunc is None:
                self.niSync_SetTime_cfunc = self._library.niSync_SetTime
                self.niSync_SetTime_cfunc.argtypes = [
                    ViSession,
                    ViInt32,
                    ViUInt32,
                    ViUInt32,
                    ViUInt16,
                ]  # noqa: F405
                self.niSync_SetTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetTime_cfunc(
            vi, timeSource, timeSeconds, timeNanoseconds, timeFractionalNanoseconds
        )

    def niSync_GetTime(
        self, vi, timeSeconds, timeNanoseconds, timeFractionalNanoseconds
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_GetTime_cfunc is None:
                self.niSync_GetTime_cfunc = self._library.niSync_GetTime
                self.niSync_GetTime_cfunc.argtypes = [
                    ViSession,
                    ctypes.POINTER(ViUInt32),
                    ctypes.POINTER(ViUInt32),
                    ctypes.POINTER(ViUInt16),
                ]  # noqa: F405
                self.niSync_GetTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetTime_cfunc(
            vi, timeSeconds, timeNanoseconds, timeFractionalNanoseconds
        )

    def niSync_ResetFrequency(self, vi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_ResetFrequency_cfunc is None:
                self.niSync_ResetFrequency_cfunc = self._library.niSync_ResetFrequency
                self.niSync_ResetFrequency_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_ResetFrequency_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ResetFrequency_cfunc(vi)

    def niSync_CreateFutureTimeEvent(
        self, vi, terminal, outputLevel, timeSeconds, timeNanoseconds, timeFractionalNanoseconds
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_CreateFutureTimeEvent_cfunc is None:
                self.niSync_CreateFutureTimeEvent_cfunc = self._library.niSync_CreateFutureTimeEvent
                self.niSync_CreateFutureTimeEvent_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViInt32,
                    ViUInt32,
                    ViUInt32,
                    ViUInt16,
                ]  # noqa: F405
                self.niSync_CreateFutureTimeEvent_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_CreateFutureTimeEvent_cfunc(
            vi,
            ascii_encode(terminal),
            outputLevel,
            timeSeconds,
            timeNanoseconds,
            timeFractionalNanoseconds,
        )

    def niSync_ClearFutureTimeEvents(self, vi, terminal):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_ClearFutureTimeEvents_cfunc is None:
                self.niSync_ClearFutureTimeEvents_cfunc = self._library.niSync_ClearFutureTimeEvents
                self.niSync_ClearFutureTimeEvents_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                ]  # noqa: F405
                self.niSync_ClearFutureTimeEvents_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ClearFutureTimeEvents_cfunc(vi, ascii_encode(terminal))

    def niSync_EnableTimeStampTrigger(self, vi, terminal, activeEdge):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_EnableTimeStampTrigger_cfunc is None:
                self.niSync_EnableTimeStampTrigger_cfunc = (
                    self._library.niSync_EnableTimeStampTrigger
                )
                self.niSync_EnableTimeStampTrigger_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViInt32,
                ]  # noqa: F405
                self.niSync_EnableTimeStampTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_EnableTimeStampTrigger_cfunc(vi, ascii_encode(terminal), activeEdge)

    def niSync_EnableTimeStampTriggerWithDecimation(
        self, vi, terminal, activeEdge, decimationCount
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_EnableTimeStampTriggerWithDecimation_cfunc is None:
                self.niSync_EnableTimeStampTriggerWithDecimation_cfunc = (
                    self._library.niSync_EnableTimeStampTriggerWithDecimation
                )
                self.niSync_EnableTimeStampTriggerWithDecimation_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViInt32,
                    ViUInt32,
                ]  # noqa: F405
                self.niSync_EnableTimeStampTriggerWithDecimation_cfunc.restype = (
                    ViStatus  # noqa: F405
                )
        return self.niSync_EnableTimeStampTriggerWithDecimation_cfunc(
            vi, ascii_encode(terminal), activeEdge, decimationCount
        )

    def niSync_ReadTriggerTimeStamp(
        self,
        vi,
        terminal,
        timeout,
        timeSeconds,
        timeNanoseconds,
        timeFractionalNanoseconds,
        detectedEdge,
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_ReadTriggerTimeStamp_cfunc is None:
                self.niSync_ReadTriggerTimeStamp_cfunc = self._library.niSync_ReadTriggerTimeStamp
                self.niSync_ReadTriggerTimeStamp_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViReal64,
                    ctypes.POINTER(ViUInt32),
                    ctypes.POINTER(ViUInt32),
                    ctypes.POINTER(ViUInt16),
                    ctypes.POINTER(ViInt32),
                ]  # noqa: F405
                self.niSync_ReadTriggerTimeStamp_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ReadTriggerTimeStamp_cfunc(
            vi,
            ascii_encode(terminal),
            timeout,
            timeSeconds,
            timeNanoseconds,
            timeFractionalNanoseconds,
            detectedEdge,
        )

    def niSync_ReadMultipleTriggerTimeStamp(
        self,
        vi,
        terminal,
        timestampsToRead,
        timeout,
        timeSecondsBuffer,
        timeNanosecondsBuffer,
        timeFractionalNanosecondsBuffer,
        detectedEdgeBuffer,
        timestampsRead,
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_ReadMultipleTriggerTimeStamp_cfunc is None:
                self.niSync_ReadMultipleTriggerTimeStamp_cfunc = (
                    self._library.niSync_ReadMultipleTriggerTimeStamp
                )
                self.niSync_ReadMultipleTriggerTimeStamp_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViUInt32,
                    ViReal64,
                    ctypes.POINTER(ViUInt32),
                    ctypes.POINTER(ViUInt32),
                    ctypes.POINTER(ViUInt16),
                    ctypes.POINTER(ViInt32),
                    ctypes.POINTER(ViUInt32),
                ]  # noqa: F405
                self.niSync_ReadMultipleTriggerTimeStamp_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ReadMultipleTriggerTimeStamp_cfunc(
            vi,
            ascii_encode(terminal),
            timestampsToRead,
            timeout,
            timeSecondsBuffer,
            timeNanosecondsBuffer,
            timeFractionalNanosecondsBuffer,
            detectedEdgeBuffer,
            timestampsRead,
        )

    def niSync_DisableTimeStampTrigger(self, vi, terminal):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_DisableTimeStampTrigger_cfunc is None:
                self.niSync_DisableTimeStampTrigger_cfunc = (
                    self._library.niSync_DisableTimeStampTrigger
                )
                self.niSync_DisableTimeStampTrigger_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                ]  # noqa: F405
                self.niSync_DisableTimeStampTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_DisableTimeStampTrigger_cfunc(vi, ascii_encode(terminal))

    def niSync_CreateClock(
        self,
        vi,
        terminal,
        highTicks,
        lowTicks,
        startTimeSeconds,
        startTimeNanoseconds,
        startTimeFractionalNanoseconds,
        stopTimeSeconds,
        stopTimeNanoseconds,
        stopTimeFractionalNanoseconds,
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_CreateClock_cfunc is None:
                self.niSync_CreateClock_cfunc = self._library.niSync_CreateClock
                self.niSync_CreateClock_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViUInt32,
                    ViUInt32,
                    ViUInt32,
                    ViUInt32,
                    ViUInt16,
                    ViUInt32,
                    ViUInt32,
                    ViUInt16,
                ]  # noqa: F405
                self.niSync_CreateClock_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_CreateClock_cfunc(
            vi,
            ascii_encode(terminal),
            highTicks,
            lowTicks,
            startTimeSeconds,
            startTimeNanoseconds,
            startTimeFractionalNanoseconds,
            stopTimeSeconds,
            stopTimeNanoseconds,
            stopTimeFractionalNanoseconds,
        )

    def niSync_ClearClock(self, vi, terminal):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_ClearClock_cfunc is None:
                self.niSync_ClearClock_cfunc = self._library.niSync_ClearClock
                self.niSync_ClearClock_cfunc.argtypes = [ViSession, ViConstString]  # noqa: F405
                self.niSync_ClearClock_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ClearClock_cfunc(vi, ascii_encode(terminal))

    def niSync_Start8021AS(self, vi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_Start8021AS_cfunc is None:
                self.niSync_Start8021AS_cfunc = self._library.niSync_Start8021AS
                self.niSync_Start8021AS_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_Start8021AS_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_Start8021AS_cfunc(vi)

    def niSync_Stop8021AS(self, vi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_Stop8021AS_cfunc is None:
                self.niSync_Stop8021AS_cfunc = self._library.niSync_Stop8021AS
                self.niSync_Stop8021AS_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_Stop8021AS_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_Stop8021AS_cfunc(vi)

    def niSync_SetTimeReferenceFreeRunning(self, vi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_SetTimeReferenceFreeRunning_cfunc is None:
                self.niSync_SetTimeReferenceFreeRunning_cfunc = (
                    self._library.niSync_SetTimeReferenceFreeRunning
                )
                self.niSync_SetTimeReferenceFreeRunning_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_SetTimeReferenceFreeRunning_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetTimeReferenceFreeRunning_cfunc(vi)

    def niSync_SetTimeReferenceGPS(self, vi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_SetTimeReferenceGPS_cfunc is None:
                self.niSync_SetTimeReferenceGPS_cfunc = self._library.niSync_SetTimeReferenceGPS
                self.niSync_SetTimeReferenceGPS_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_SetTimeReferenceGPS_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetTimeReferenceGPS_cfunc(vi)

    def niSync_SetTimeReferenceIRIG(self, vi, irigType, terminalName):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_SetTimeReferenceIRIG_cfunc is None:
                self.niSync_SetTimeReferenceIRIG_cfunc = self._library.niSync_SetTimeReferenceIRIG
                self.niSync_SetTimeReferenceIRIG_cfunc.argtypes = [
                    ViSession,
                    ViInt32,
                    ViConstString,
                ]  # noqa: F405
                self.niSync_SetTimeReferenceIRIG_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetTimeReferenceIRIG_cfunc(vi, irigType, ascii_encode(terminalName))

    def niSync_SetTimeReferencePPS(
        self,
        vi,
        terminalName,
        useManualTime,
        initialTimeSeconds,
        initialTimeNanoseconds,
        initialTimeFractionalNanoseconds,
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_SetTimeReferencePPS_cfunc is None:
                self.niSync_SetTimeReferencePPS_cfunc = self._library.niSync_SetTimeReferencePPS
                self.niSync_SetTimeReferencePPS_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViBoolean,
                    ViUInt32,
                    ViUInt32,
                    ViUInt16,
                ]  # noqa: F405
                self.niSync_SetTimeReferencePPS_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetTimeReferencePPS_cfunc(
            vi,
            ascii_encode(terminalName),
            useManualTime,
            initialTimeSeconds,
            initialTimeNanoseconds,
            initialTimeFractionalNanoseconds,
        )

    def niSync_SetTimeReference1588OrdinaryClock(self, vi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_SetTimeReference1588OrdinaryClock_cfunc is None:
                self.niSync_SetTimeReference1588OrdinaryClock_cfunc = (
                    self._library.niSync_SetTimeReference1588OrdinaryClock
                )
                self.niSync_SetTimeReference1588OrdinaryClock_cfunc.argtypes = [
                    ViSession
                ]  # noqa: F405
                self.niSync_SetTimeReference1588OrdinaryClock_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetTimeReference1588OrdinaryClock_cfunc(vi)

    def niSync_SetTimeReference8021AS(self, vi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_SetTimeReference8021AS_cfunc is None:
                self.niSync_SetTimeReference8021AS_cfunc = (
                    self._library.niSync_SetTimeReference8021AS
                )
                self.niSync_SetTimeReference8021AS_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_SetTimeReference8021AS_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetTimeReference8021AS_cfunc(vi)

    def niSync_EnableGPSTimestamping(self, vi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_EnableGPSTimestamping_cfunc is None:
                self.niSync_EnableGPSTimestamping_cfunc = self._library.niSync_EnableGPSTimestamping
                self.niSync_EnableGPSTimestamping_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_EnableGPSTimestamping_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_EnableGPSTimestamping_cfunc(vi)

    def niSync_EnableIRIGTimestamping(self, vi, irigType, terminalName):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_EnableIRIGTimestamping_cfunc is None:
                self.niSync_EnableIRIGTimestamping_cfunc = (
                    self._library.niSync_EnableIRIGTimestamping
                )
                self.niSync_EnableIRIGTimestamping_cfunc.argtypes = [
                    ViSession,
                    ViInt32,
                    ViConstString,
                ]  # noqa: F405
                self.niSync_EnableIRIGTimestamping_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_EnableIRIGTimestamping_cfunc(vi, irigType, ascii_encode(terminalName))

    def niSync_ReadLastGPSTimestamp(
        self,
        vi,
        timestampSeconds,
        timestampNanoseconds,
        timestampFractionalNanoseconds,
        gpsSeconds,
        gpsNanoseconds,
        gpsFractionalNanoseconds,
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_ReadLastGPSTimestamp_cfunc is None:
                self.niSync_ReadLastGPSTimestamp_cfunc = self._library.niSync_ReadLastGPSTimestamp
                self.niSync_ReadLastGPSTimestamp_cfunc.argtypes = [
                    ViSession,
                    ctypes.POINTER(ViUInt32),
                    ctypes.POINTER(ViUInt32),
                    ctypes.POINTER(ViUInt16),
                    ctypes.POINTER(ViUInt32),
                    ctypes.POINTER(ViUInt32),
                    ctypes.POINTER(ViUInt16),
                ]  # noqa: F405
                self.niSync_ReadLastGPSTimestamp_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ReadLastGPSTimestamp_cfunc(
            vi,
            timestampSeconds,
            timestampNanoseconds,
            timestampFractionalNanoseconds,
            gpsSeconds,
            gpsNanoseconds,
            gpsFractionalNanoseconds,
        )

    def niSync_ReadLastIRIGTimestamp(
        self,
        vi,
        terminal,
        timestampSeconds,
        timestampNanoseconds,
        timestampFractionalNanoseconds,
        irigbSeconds,
        irigbNanoseconds,
        irigbFractionalNanoseconds,
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_ReadLastIRIGTimestamp_cfunc is None:
                self.niSync_ReadLastIRIGTimestamp_cfunc = self._library.niSync_ReadLastIRIGTimestamp
                self.niSync_ReadLastIRIGTimestamp_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ctypes.POINTER(ViUInt32),
                    ctypes.POINTER(ViUInt32),
                    ctypes.POINTER(ViUInt16),
                    ctypes.POINTER(ViUInt32),
                    ctypes.POINTER(ViUInt32),
                    ctypes.POINTER(ViUInt16),
                ]  # noqa: F405
                self.niSync_ReadLastIRIGTimestamp_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ReadLastIRIGTimestamp_cfunc(
            vi,
            ascii_encode(terminal),
            timestampSeconds,
            timestampNanoseconds,
            timestampFractionalNanoseconds,
            irigbSeconds,
            irigbNanoseconds,
            irigbFractionalNanoseconds,
        )

    def niSync_DisableGPSTimestamping(self, vi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_DisableGPSTimestamping_cfunc is None:
                self.niSync_DisableGPSTimestamping_cfunc = (
                    self._library.niSync_DisableGPSTimestamping
                )
                self.niSync_DisableGPSTimestamping_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_DisableGPSTimestamping_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_DisableGPSTimestamping_cfunc(vi)

    def niSync_DisableIRIGTimestamping(self, vi, terminalName):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_DisableIRIGTimestamping_cfunc is None:
                self.niSync_DisableIRIGTimestamping_cfunc = (
                    self._library.niSync_DisableIRIGTimestamping
                )
                self.niSync_DisableIRIGTimestamping_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                ]  # noqa: F405
                self.niSync_DisableIRIGTimestamping_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_DisableIRIGTimestamping_cfunc(vi, ascii_encode(terminalName))

    def niSync_GetVelocity(self, vi, eastVelocity, northVelocity, upVelocity):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_GetVelocity_cfunc is None:
                self.niSync_GetVelocity_cfunc = self._library.niSync_GetVelocity
                self.niSync_GetVelocity_cfunc.argtypes = [
                    ViSession,
                    ctypes.POINTER(ViReal64),
                    ctypes.POINTER(ViReal64),
                    ctypes.POINTER(ViReal64),
                ]  # noqa: F405
                self.niSync_GetVelocity_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetVelocity_cfunc(vi, eastVelocity, northVelocity, upVelocity)

    def niSync_GetLocation(self, vi, latitude, longitude, altitude):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_GetLocation_cfunc is None:
                self.niSync_GetLocation_cfunc = self._library.niSync_GetLocation
                self.niSync_GetLocation_cfunc.argtypes = [
                    ViSession,
                    ctypes.POINTER(ViReal64),
                    ctypes.POINTER(ViReal64),
                    ctypes.POINTER(ViReal64),
                ]  # noqa: F405
                self.niSync_GetLocation_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetLocation_cfunc(vi, latitude, longitude, altitude)

    def niSync_GetAttributeViInt32(self, vi, activeItem, attribute, value):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_GetAttributeViInt32_cfunc is None:
                self.niSync_GetAttributeViInt32_cfunc = self._library.niSync_GetAttributeViInt32
                self.niSync_GetAttributeViInt32_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViAttr,
                    ctypes.POINTER(ViInt32),
                ]  # noqa: F405
                self.niSync_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetAttributeViInt32_cfunc(vi, ascii_encode(activeItem), attribute, value)

    def niSync_GetAttributeViReal64(self, vi, activeItem, attribute, value):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_GetAttributeViReal64_cfunc is None:
                self.niSync_GetAttributeViReal64_cfunc = self._library.niSync_GetAttributeViReal64
                self.niSync_GetAttributeViReal64_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViAttr,
                    ctypes.POINTER(ViReal64),
                ]  # noqa: F405
                self.niSync_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetAttributeViReal64_cfunc(
            vi, ascii_encode(activeItem), attribute, value
        )

    def niSync_GetAttributeViBoolean(self, vi, activeItem, attribute, value):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_GetAttributeViBoolean_cfunc is None:
                self.niSync_GetAttributeViBoolean_cfunc = self._library.niSync_GetAttributeViBoolean
                self.niSync_GetAttributeViBoolean_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViAttr,
                    ctypes.POINTER(ViBoolean),
                ]  # noqa: F405
                self.niSync_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetAttributeViBoolean_cfunc(
            vi, ascii_encode(activeItem), attribute, value
        )

    def niSync_GetAttributeViString(
        self, vi, activeItem, attribute, bufferSize, value
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_GetAttributeViString_cfunc is None:
                self.niSync_GetAttributeViString_cfunc = self._library.niSync_GetAttributeViString
                self.niSync_GetAttributeViString_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViAttr,
                    ViInt32,
                    ctypes.POINTER(ViChar),
                ]  # noqa: F405
                self.niSync_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetAttributeViString_cfunc(
            vi, ascii_encode(activeItem), attribute, bufferSize, value
        )

    def niSync_SetAttributeViInt32(self, vi, activeItem, attribute, value):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_SetAttributeViInt32_cfunc is None:
                self.niSync_SetAttributeViInt32_cfunc = self._library.niSync_SetAttributeViInt32
                self.niSync_SetAttributeViInt32_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViAttr,
                    ViInt32,
                ]  # noqa: F405
                self.niSync_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetAttributeViInt32_cfunc(vi, ascii_encode(activeItem), attribute, value)

    def niSync_SetAttributeViReal64(self, vi, activeItem, attribute, value):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_SetAttributeViReal64_cfunc is None:
                self.niSync_SetAttributeViReal64_cfunc = self._library.niSync_SetAttributeViReal64
                self.niSync_SetAttributeViReal64_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViAttr,
                    ViReal64,
                ]  # noqa: F405
                self.niSync_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetAttributeViReal64_cfunc(
            vi, ascii_encode(activeItem), attribute, value
        )

    def niSync_SetAttributeViBoolean(self, vi, activeItem, attribute, value):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_SetAttributeViBoolean_cfunc is None:
                self.niSync_SetAttributeViBoolean_cfunc = self._library.niSync_SetAttributeViBoolean
                self.niSync_SetAttributeViBoolean_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViAttr,
                    ViBoolean,
                ]  # noqa: F405
                self.niSync_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetAttributeViBoolean_cfunc(
            vi, ascii_encode(activeItem), attribute, value
        )

    def niSync_SetAttributeViString(self, vi, activeItem, attribute, value):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_SetAttributeViString_cfunc is None:
                self.niSync_SetAttributeViString_cfunc = self._library.niSync_SetAttributeViString
                self.niSync_SetAttributeViString_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViAttr,
                    ViConstString,
                ]  # noqa: F405
                self.niSync_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_SetAttributeViString_cfunc(
            vi, ascii_encode(activeItem), attribute, ascii_encode(value)
        )

    def niSync_GetExtCalLastDateAndTime(
        self, vi, year, month, day, hour, minute
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_GetExtCalLastDateAndTime_cfunc is None:
                self.niSync_GetExtCalLastDateAndTime_cfunc = (
                    self._library.niSync_GetExtCalLastDateAndTime
                )
                self.niSync_GetExtCalLastDateAndTime_cfunc.argtypes = [
                    ViSession,
                    ctypes.POINTER(ViInt32),
                    ctypes.POINTER(ViInt32),
                    ctypes.POINTER(ViInt32),
                    ctypes.POINTER(ViInt32),
                    ctypes.POINTER(ViInt32),
                ]  # noqa: F405
                self.niSync_GetExtCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetExtCalLastDateAndTime_cfunc(vi, year, month, day, hour, minute)

    def niSync_GetExtCalLastTemp(self, vi, temp):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_GetExtCalLastTemp_cfunc is None:
                self.niSync_GetExtCalLastTemp_cfunc = self._library.niSync_GetExtCalLastTemp
                self.niSync_GetExtCalLastTemp_cfunc.argtypes = [
                    ViSession,
                    ctypes.POINTER(ViReal64),
                ]  # noqa: F405
                self.niSync_GetExtCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetExtCalLastTemp_cfunc(vi, temp)

    def niSync_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_GetExtCalRecommendedInterval_cfunc is None:
                self.niSync_GetExtCalRecommendedInterval_cfunc = (
                    self._library.niSync_GetExtCalRecommendedInterval
                )
                self.niSync_GetExtCalRecommendedInterval_cfunc.argtypes = [
                    ViSession,
                    ctypes.POINTER(ViInt32),
                ]  # noqa: F405
                self.niSync_GetExtCalRecommendedInterval_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_GetExtCalRecommendedInterval_cfunc(vi, months)

    def niSync_ChangeExtCalPassword(self, vi, oldPassword, newPassword):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_ChangeExtCalPassword_cfunc is None:
                self.niSync_ChangeExtCalPassword_cfunc = self._library.niSync_ChangeExtCalPassword
                self.niSync_ChangeExtCalPassword_cfunc.argtypes = [
                    ViSession,
                    ViConstString,
                    ViConstString,
                ]  # noqa: F405
                self.niSync_ChangeExtCalPassword_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ChangeExtCalPassword_cfunc(
            vi, ascii_encode(oldPassword), ascii_encode(newPassword)
        )

    def niSync_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_ReadCurrentTemperature_cfunc is None:
                self.niSync_ReadCurrentTemperature_cfunc = (
                    self._library.niSync_ReadCurrentTemperature
                )
                self.niSync_ReadCurrentTemperature_cfunc.argtypes = [
                    ViSession,
                    ctypes.POINTER(ViReal64),
                ]  # noqa: F405
                self.niSync_ReadCurrentTemperature_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_ReadCurrentTemperature_cfunc(vi, temperature)

    def niSync_CalGetOscillatorVoltage(self, vi, voltage):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_CalGetOscillatorVoltage_cfunc is None:
                self.niSync_CalGetOscillatorVoltage_cfunc = (
                    self._library.niSync_CalGetOscillatorVoltage
                )
                self.niSync_CalGetOscillatorVoltage_cfunc.argtypes = [
                    ViSession,
                    ctypes.POINTER(ViReal64),
                ]  # noqa: F405
                self.niSync_CalGetOscillatorVoltage_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_CalGetOscillatorVoltage_cfunc(vi, voltage)

    def niSync_CalGetClk10PhaseVoltage(self, vi, voltage):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_CalGetClk10PhaseVoltage_cfunc is None:
                self.niSync_CalGetClk10PhaseVoltage_cfunc = (
                    self._library.niSync_CalGetClk10PhaseVoltage
                )
                self.niSync_CalGetClk10PhaseVoltage_cfunc.argtypes = [
                    ViSession,
                    ctypes.POINTER(ViReal64),
                ]  # noqa: F405
                self.niSync_CalGetClk10PhaseVoltage_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_CalGetClk10PhaseVoltage_cfunc(vi, voltage)

    def niSync_CalGetDDSStartPulsePhaseVoltage(self, vi, voltage):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_CalGetDDSStartPulsePhaseVoltage_cfunc is None:
                self.niSync_CalGetDDSStartPulsePhaseVoltage_cfunc = (
                    self._library.niSync_CalGetDDSStartPulsePhaseVoltage
                )
                self.niSync_CalGetDDSStartPulsePhaseVoltage_cfunc.argtypes = [
                    ViSession,
                    ctypes.POINTER(ViReal64),
                ]  # noqa: F405
                self.niSync_CalGetDDSStartPulsePhaseVoltage_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_CalGetDDSStartPulsePhaseVoltage_cfunc(vi, voltage)

    def niSync_CalGetDDSInitialPhase(self, vi, phase):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_CalGetDDSInitialPhase_cfunc is None:
                self.niSync_CalGetDDSInitialPhase_cfunc = self._library.niSync_CalGetDDSInitialPhase
                self.niSync_CalGetDDSInitialPhase_cfunc.argtypes = [
                    ViSession,
                    ctypes.POINTER(ViReal64),
                ]  # noqa: F405
                self.niSync_CalGetDDSInitialPhase_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_CalGetDDSInitialPhase_cfunc(vi, phase)

    def niSync_InitExtCal(self, resourceName, password, extCalVi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_InitExtCal_cfunc is None:
                self.niSync_InitExtCal_cfunc = self._library.niSync_InitExtCal
                self.niSync_InitExtCal_cfunc.argtypes = [
                    ViRsrc,
                    ViConstString,
                    ctypes.POINTER(ViSession),
                ]  # noqa: F405
                self.niSync_InitExtCal_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_InitExtCal_cfunc(
            ascii_encode(resourceName), ascii_encode(password), extCalVi
        )

    def niSync_CloseExtCal(self, extCalVi, action):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_CloseExtCal_cfunc is None:
                self.niSync_CloseExtCal_cfunc = self._library.niSync_CloseExtCal
                self.niSync_CloseExtCal_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niSync_CloseExtCal_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_CloseExtCal_cfunc(extCalVi, action)

    def niSync_CalAdjustOscillatorVoltage(
        self, extCalVi, measuredVoltage, oldVoltage
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_CalAdjustOscillatorVoltage_cfunc is None:
                self.niSync_CalAdjustOscillatorVoltage_cfunc = (
                    self._library.niSync_CalAdjustOscillatorVoltage
                )
                self.niSync_CalAdjustOscillatorVoltage_cfunc.argtypes = [
                    ViSession,
                    ViReal64,
                    ctypes.POINTER(ViReal64),
                ]  # noqa: F405
                self.niSync_CalAdjustOscillatorVoltage_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_CalAdjustOscillatorVoltage_cfunc(extCalVi, measuredVoltage, oldVoltage)

    def niSync_CalAdjustClk10PhaseVoltage(
        self, extCalVi, measuredVoltage, oldVoltage
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_CalAdjustClk10PhaseVoltage_cfunc is None:
                self.niSync_CalAdjustClk10PhaseVoltage_cfunc = (
                    self._library.niSync_CalAdjustClk10PhaseVoltage
                )
                self.niSync_CalAdjustClk10PhaseVoltage_cfunc.argtypes = [
                    ViSession,
                    ViReal64,
                    ctypes.POINTER(ViReal64),
                ]  # noqa: F405
                self.niSync_CalAdjustClk10PhaseVoltage_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_CalAdjustClk10PhaseVoltage_cfunc(extCalVi, measuredVoltage, oldVoltage)

    def niSync_CalAdjustDDSStartPulsePhaseVoltage(
        self, extCalVi, measuredVoltage, oldVoltage
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_CalAdjustDDSStartPulsePhaseVoltage_cfunc is None:
                self.niSync_CalAdjustDDSStartPulsePhaseVoltage_cfunc = (
                    self._library.niSync_CalAdjustDDSStartPulsePhaseVoltage
                )
                self.niSync_CalAdjustDDSStartPulsePhaseVoltage_cfunc.argtypes = [
                    ViSession,
                    ViReal64,
                    ctypes.POINTER(ViReal64),
                ]  # noqa: F405
                self.niSync_CalAdjustDDSStartPulsePhaseVoltage_cfunc.restype = (
                    ViStatus  # noqa: F405
                )
        return self.niSync_CalAdjustDDSStartPulsePhaseVoltage_cfunc(
            extCalVi, measuredVoltage, oldVoltage
        )

    def niSync_CalAdjustDDSInitialPhase(self, extCalVi, measuredPhase, oldPhase):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_CalAdjustDDSInitialPhase_cfunc is None:
                self.niSync_CalAdjustDDSInitialPhase_cfunc = (
                    self._library.niSync_CalAdjustDDSInitialPhase
                )
                self.niSync_CalAdjustDDSInitialPhase_cfunc.argtypes = [
                    ViSession,
                    ViReal64,
                    ctypes.POINTER(ViReal64),
                ]  # noqa: F405
                self.niSync_CalAdjustDDSInitialPhase_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_CalAdjustDDSInitialPhase_cfunc(extCalVi, measuredPhase, oldPhase)

    def niSync_StartPTP(
        self,
        vi,
        initialTimeSource,
        initialTimeSeconds,
        initialTimeNanoseconds,
        initialTimeFractionalNanoseconds,
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_StartPTP_cfunc is None:
                self.niSync_StartPTP_cfunc = self._library.niSync_StartPTP
                self.niSync_StartPTP_cfunc.argtypes = [
                    ViSession,
                    ViInt32,
                    ViUInt32,
                    ViUInt32,
                    ViUInt16,
                ]  # noqa: F405
                self.niSync_StartPTP_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_StartPTP_cfunc(
            vi,
            initialTimeSource,
            initialTimeSeconds,
            initialTimeNanoseconds,
            initialTimeFractionalNanoseconds,
        )

    def niSync_StopPTP(self, vi):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_StopPTP_cfunc is None:
                self.niSync_StopPTP_cfunc = self._library.niSync_StopPTP
                self.niSync_StopPTP_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niSync_StopPTP_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_StopPTP_cfunc(vi)

    def niSync_Get1588Time(
        self, vi, timeSeconds, timeNanoseconds, timeFractionalNanoseconds
    ):  # noqa: N802,N803
        with self._func_lock:
            if self.niSync_Get1588Time_cfunc is None:
                self.niSync_Get1588Time_cfunc = self._library.niSync_Get1588Time
                self.niSync_Get1588Time_cfunc.argtypes = [
                    ViSession,
                    ctypes.POINTER(ViUInt32),
                    ctypes.POINTER(ViUInt32),
                    ctypes.POINTER(ViUInt16),
                ]  # noqa: F405
                self.niSync_Get1588Time_cfunc.restype = ViStatus  # noqa: F405
        return self.niSync_Get1588Time_cfunc(
            vi, timeSeconds, timeNanoseconds, timeFractionalNanoseconds
        )
