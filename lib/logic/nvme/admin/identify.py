
from abc import ABCMeta, abstractmethod
import sys
sys.path.append("../../../../")
from lib.driver.utils.utils import *
from lib.driver.nvme.nvme import NVMe
from lib.driver.utils.buffer import Buffer
from lib.driver.data_structures.identify import *


class Identify(object):
    __metaclass__ = ABCMeta

    def __init__(self, buffer_type, buffer_length, dev_name="/dev/nvme0", **kwargs):
        self.buffer_type = buffer_type
        self.buffer_length = buffer_length
        self.data = Buffer(length=self.buffer_length, buf_type=self.buffer_type)
        self.nvme_device = NVMe(dev_name)
        self.result = self.get_identify(**kwargs)
        self.identify = self.convert()

    def get_identify(self, **kwargs):
        return None

    @property
    def identify_data(self):
        return self.identify

    @property
    def identify_result(self):
        return self.result

    def convert(self):
        return self.data.convert(self.buffer_type)

    def printf(self):
        print_structure(self.identify)


class IdentifyList(Identify):
    def __init__(self, buffer_type, buffer_length, dev_name="/dev/nvme0", **kwargs):
        super(IdentifyList, self).__init__(buffer_type, buffer_length, dev_name, **kwargs)

    def printf(self):
        for i in range(self.buffer_length):
            print("namespace id: {} is 0x{:x}".format(i, self.identify[i]))

    def convert(self):
        return self.data.cast(self.buffer_type)

class IdentifyNamespace(Identify):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(IdentifyNamespace, self).__init__(NamespaceDataStructure, 1, dev_name, **kwargs)

    def get_identify(self, **kwargs):
        nsid = kwargs["nsid"]
        result = self.nvme_device.nvme_identify_ns(nsid, False, self.data.get_buffer())
        return result


class IdentifyController(Identify):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(IdentifyController, self).__init__(ControllerDataStructure, 1, dev_name, **kwargs)

    def get_identify(self, **kwargs):
        result = self.nvme_device.nvme_identify_ctrl(self.data.get_buffer())
        return result


class IdentifyActiveNamespaceList(IdentifyList):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(IdentifyActiveNamespaceList, self).__init__(c_uint32, 1024, dev_name, **kwargs)

    def get_identify(self, **kwargs):
        result = self.nvme_device.nvme_identify_active_namespace_list(0, self.data.get_buffer())
        return result


class IdentifyAllocatedNamespaceList(IdentifyList):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(IdentifyAllocatedNamespaceList, self).__init__(c_uint32, 1024, dev_name, **kwargs)

    def get_identify(self, **kwargs):
        result = self.nvme_device.nvme_identify_all_namespace_list(0, self.data.get_buffer())
        return result


class IdentifyDescriptorList(IdentifyList):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(IdentifyDescriptorList, self).__init__(c_uint32, 1024, dev_name, **kwargs)

    def get_identify(self, **kwargs):
        nsid = kwargs["nsid"]
        result = self.nvme_device.nvme_identification_descriptor_list(nsid, self.data.get_buffer())
        return result


class IdentifyAttachedControllerList(IdentifyList):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(IdentifyAttachedControllerList, self).__init__(c_uint32, 1024, dev_name, **kwargs)

    def get_identify(self, **kwargs):
        nsid = kwargs["nsid"]
        cntid = kwargs["cntid"]
        result = self.nvme_device.nvme_identify_ctrl_list(nsid, cntid, self.data.get_buffer())
        return result


class IdentifyControllerList(IdentifyList):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(IdentifyControllerList, self).__init__(c_uint32, 1024, dev_name, **kwargs)

    def get_identify(self, **kwargs):
        cntid = kwargs["cntid"]
        result = self.nvme_device.nvme_identify_ctrl_list(0, cntid, self.data.get_buffer())
        return result


class IdentifyAllocatedNamespace(Identify):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(IdentifyAllocatedNamespace, self).__init__(NamespaceDataStructure, 1, dev_name, **kwargs)

    def get_identify(self, **kwargs):
        nsid = kwargs["nsid"]
        result = self.nvme_device.nvme_identify_ns(nsid, True, self.data.get_buffer())
        return result


class IdentifyPrimaryCtrlData(Identify):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(IdentifyPrimaryCtrlData, self).__init__(PrimaryControllerCap, 1 ,dev_name, **kwargs)

    def get_identify(self, **kwargs):
        result = self.nvme_device.nvme_identify(0, 0x13, self.data.get_buffer())
        return result


class SecondaryCtrlList(Identify):
    def __init__(self, dev_name="/dev/nvme0", **kwargs):
        super(SecondaryCtrlList, self).__init__(SecondaryControllerList, 1, dev_name, **kwargs)

    def get_identify(self, **kwargs):
        nsid = kwargs["nsid"]
        cntid = kwargs["cntid"]
        result = self.nvme_device.nvme_identify_secondary_ctrl_list(nsid, cntid, self.data.get_buffer())
        return result
