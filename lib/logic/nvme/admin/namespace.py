

from ctypes import c_uint32, c_uint16
from lib.driver.nvme.nvme import NVMe
from lib.driver.utils.buffer import Buffer


class NameSpace(object):


    def __init__(self, nsid=None, dev_name="/dev/nvme0"):
        self.nvme_device = NVMe(dev_name)
        self.nsid = nsid

    def get_nsid(self):
        return self.nsid

    def set_nsid(self, nsid):
        self.nsid = nsid

    def create_namespace(self, nsze, ncap, flbas, dps=0, nmic=0, timeout=10):
        pdata = Buffer(1, c_uint32)
        ret =self.nvme_device.nvme_ns_create(nsze, ncap, flbas, dps, nmic, timeout, pdata.get_buffer())
        self.nsid = pdata.convert(c_uint32)
        return ret

    def delete_namespace(self, nsid, timeout=10):
        return self.nvme_device.nvme_ns_delete(nsid, timeout)

    def attach(self, ctrl_list):
        num_ctrls = len(ctrl_list)
        ctrl_list_data = Buffer(num_ctrls, c_uint16)
        pdata = ctrl_list_data.get_buffer()
        for index in range(num_ctrls):
            pdata[index] = ctrl_list[index]
        return self.nvme_device.nvme_ns_attach_ctrls(self.nsid, num_ctrls, pdata)

    def detach(self, ctrl_list):
        num_ctrls = len(ctrl_list)
        ctrl_list_data = Buffer(num_ctrls, c_uint16)
        pdata = ctrl_list_data.get_buffer()
        for index in range(num_ctrls):
            pdata[index] = ctrl_list[index]
        return self.nvme_device.nvme_ns_detach_ctrls(self.nsid, num_ctrls, pdata)

    def format(self, lbaf, ms, ses=0, pi=0, pil=0):
        return self.nvme_device.nvme_format(self.nsid, lbaf, ses, pi, pil, ms, timeout=1000)

