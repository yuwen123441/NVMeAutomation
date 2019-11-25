
import sys
from abc import ABCMeta, abstractmethod
sys.path.append("../../../../")
from lib.driver.utils.utils import *
from lib.driver.nvme.nvme import NVMe
from lib.driver.data_structures.log_page import ErrorInformation as StructureErrorInfo
from lib.driver.data_structures.log_page import SmartHealth as StructureSmartHealth
from lib.driver.data_structures.log_page import FirmwareSlotInformationLog as StructureFWSlot
from lib.driver.data_structures.log_page import ChangedNamespaceList as StructureChangedNSList
from lib.driver.data_structures.log_page import CommandEffectLog as StructureCommandEffectLog
from lib.driver.data_structures.log_page import SelfTestLog as StructureSelfTestResult
from lib.driver.data_structures.log_page import TelemetryHostInitiatedLog as StructureTelemetryHost
from lib.driver.data_structures.log_page import TelemetryControllerInitiatedLog as StructureTelemetryCtrl
from lib.driver.data_structures.log_page import SanitizeStatusLog as StructureSanitizeStatusLog
from lib.driver.utils.buffer import Buffer


class LogPage(object):
    __metaclass__ = ABCMeta

    def __init__(self, buf_type, buf_length=1, dev_name="/dev/nvme0", **kwargs):
        self.buffer_type = buf_type
        self.buffer_length = buf_length
        self.data = Buffer(length=self.buffer_length, buf_type=self.buffer_type)
        self.nvme_device = NVMe(dev_name)
        self.result = self.get_log_page(**kwargs)
        self.log_page = self.data.convert(self.buffer_type)

    @property
    def log_page_data(self):
        return self.log_page

    @property
    def get_log_page_result(self):
        return self.result

    @abstractmethod
    def get_log_page(self, **kwargs):
        return None

    def printf(self):
        print_structure(self.log_page_data)


class ErrorInformation(LogPage):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(ErrorInformation, self).__init__(StructureErrorInfo, 1, dev_name, **kwargs)

    def get_log_page(self, **kwargs):
        entries = kwargs["entries"]
        result = self.nvme_device.nvme_error_log(entries,  self.data.get_buffer())
        return result


class SmartHealthInformation(LogPage):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(SmartHealthInformation, self).__init__(StructureSmartHealth, 1, dev_name, **kwargs)

    def get_log_page(self, **kwargs):
        nsid = kwargs["nsid"]
        result = self.nvme_device.nvme_smart_log(nsid, self.data.get_buffer())
        return result


class FirmwareSlotInformation(LogPage):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(FirmwareSlotInformation, self).__init__(StructureFWSlot, 1, dev_name, **kwargs)

    def get_log_page(self, **kwargs):
        result = self.nvme_device.nvme_fw_log(self.data.get_buffer())
        return result


class ChangedNSList(LogPage):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(ChangedNSList, self).__init__(StructureChangedNSList, 1, dev_name, **kwargs)

    def get_log_page(self, **kwargs):
        result = self.nvme_device.nvme_changed_ns_list_log(self.data.get_buffer())
        return result


class CommandsSupportEffects(LogPage):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(CommandsSupportEffects, self).__init__(StructureCommandEffectLog, 1, dev_name, **kwargs)

    def get_log_page(self, **kwargs):
        result = self.nvme_device.nvme_effects_log(self.data.get_buffer())
        return result


class DeviceSelfTest(LogPage):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(DeviceSelfTest, self).__init__(StructureSelfTestResult, 1, dev_name, **kwargs)

    def get_log_page(self, **kwargs):
        result = self.nvme_device.nvme_self_test_log(self.data.get_buffer())
        return result


class TelemetryHostInitLog(LogPage):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(TelemetryHostInitLog, self).__init__(StructureTelemetryHost, 1, dev_name, **kwargs)

    def get_log_page(self, **kwargs):
        ctrl_init = 0
        generate_report = 1
        log_page_size = 512
        offset = 0
        result = self.nvme_device.nvme_get_telemetry_log(generate_report, ctrl_init, log_page_size, offset, self.data.get_buffer())
        return result


class TelemetryControllerInitLog(LogPage):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(TelemetryControllerInitLog, self).__init__(StructureTelemetryCtrl, 1, dev_name, **kwargs)

    def get_log_page(self, **kwargs):
        ctrl_init = 1
        generate_report = 0
        log_page_size = 512
        offset = 0
        result = self.nvme_device.nvme_get_telemetry_log(generate_report, ctrl_init, log_page_size, offset, self.data.get_buffer())
        return result


class SanitizeStatusLog(LogPage):

    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(SanitizeStatusLog, self).__init__(StructureSanitizeStatusLog, 1, dev_name, **kwargs)

    def get_log_page(self, **kwargs):
        result = self.nvme_device.nvme_sanitize_log(self.data.get_buffer())
        return result
