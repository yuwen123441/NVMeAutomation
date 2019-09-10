

from ctypes import c_uint32, c_uint16
from lib.driver.nvme.nvme import NVMe
from lib.driver.utils.buffer import Buffer


class NameSpace(object):


    def __init__(self, dev_name="/dev/nvme0"):
        self.nvme_device = NVMe(dev_name)

    def create_namespace(self, nsze, ncap, flbas, dps=0, nmic=0, timeout=10):
        pdata = Buffer(1, c_uint32)
        ret =self.nvme_device.nvme_ns_create(nsze, ncap, flbas, dps, nmic, timeout, pdata.get_buffer())
        result = pdata.convert(c_uint32)
        return ret, result

    def delete_namespace(self, nsid, timeout=10):
        return self.nvme_device.nvme_ns_delete(nsid, timeout)

    def attach(self, nsid, ctrl_list):
        num_ctrls = len(ctrl_list)
        ctrl_list_data = Buffer(num_ctrls, c_uint16)
        pdata = ctrl_list_data.get_buffer()
        for index in range(num_ctrls):
            pdata[index] = ctrl_list[index]
        return self.nvme_device.nvme_ns_attach_ctrls(nsid, num_ctrls, pdata)

    def detach(self, nsid, ctrl_list):
        num_ctrls = len(ctrl_list)
        ctrl_list_data = Buffer(num_ctrls, c_uint16)
        pdata = ctrl_list_data.get_buffer()
        for index in range(num_ctrls):
            pdata[index] = ctrl_list[index]
        return self.nvme_device.nvme_ns_detach_ctrls(nsid, num_ctrls, pdata)