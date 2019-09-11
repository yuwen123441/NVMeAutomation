

import os
from ctypes import c_uint32, c_uint8
from lib.driver.nvme.nvme import NVMe
from lib.driver.utils.buffer import Buffer


class Firmware(object):


    def __init__(self,  dev_name="/dev/nvme0"):
        self.nvme_device = NVMe(dev_name)

    def get_firmware_buf(self, fw_path):
        size = os.path.getsize(fw_path)
        ndw = size / 4
        fw_file = open(fw_path, "rb")
        fw_data = fw_file.read()
        # f_buf = Buffer(size, c_uint8)
        # f_buf.memcopy(fw_data, 0, size)
        return ndw, id(fw_data)

    def download(self, offset, fw_path):
        length, pdata = self.get_firmware_buf(fw_path)
        return self.nvme_device.nvme_fw_download(offset, length, pdata)

    def commit(self, slot, action, bpid=0):
        return self.nvme_device.nvme_fw_commit(slot, action, bpid)



