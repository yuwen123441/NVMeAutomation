

import os
from ctypes import CDLL, sizeof, byref


class NVMe(object):

    def __init__(self, dev_name="/dev/nvme0"):
        self.driver = self.load_nvme_library()
        self.fd = self.open_dev(dev_name)

    def __del__(self):
        self.close_dev()

    def load_nvme_library(self):
        so_path = os.path.realpath(os.path.join(os.path.dirname(__file__), "nvme_library.so"))
        driver = CDLL(so_path)
        return driver

    def open_dev(self, dev_name):
        fd = self.driver.open_dev(dev_name.encode(encoding="utf-8"))
        if fd == -1:
            print("Device open error: fd:{}".format(fd))
        return fd

    def close_dev(self):
        if self.fd != -1:
            self.driver.close_dev(self.fd)

    def nvme_identify(self, nsid, cdw10, pdata):
        return self.driver.nvme_identify(self.fd, nsid, cdw10, pdata)

    def nvme_identify_ns(self, nsid, present, pdata):
        return self.driver.nvme_identify_ns(self.fd, nsid, present, pdata)

    def nvme_identify_ctrl(self, pdata):
        return self.driver.nvme_identify_ctrl(self.fd, pdata)

    def nvme_identify_all_namespace_list(self, nsid, pdata):
        return self.driver.nvme_identify_ns_list(self.fd, nsid, True, pdata)

    def nvme_identify_active_namespace_list(self, nsid, pdata):
        return self.driver.nvme_identify_ns_list(self.fd, nsid, False, pdata)

    def nvme_identification_descriptor_list(self, nsid, pdata):
        return self.driver.nvme_identify_ns_descs(self.fd, nsid, pdata)

    def nvme_identify_ctrl_list(self, nsid, cntid, pdata):
        return  self.driver.nvme_identify_ctrl_list(self.fd, nsid, cntid, pdata)

    def nvme_identify_secondary_ctrl_list(self, nsid, cntid, pdata):
        return  self.driver.nvme_identify_secondary_ctrl_list(self.fd, nsid, cntid, pdata)

    def nvme_error_log(self, entries, pdata):
        return self.driver.nvme_error_log(self.fd, entries, pdata)

    def nvme_smart_log(self, nsid, pdata):
        return self.driver.nvme_smart_log(self.fd, nsid, pdata)

    def nvme_fw_log(self, pdata):
        return self.driver.nvme_fw_log(self.fd, pdata)

    def nvme_changed_ns_list_log(self, pdata):
        return self.driver.nvme_changed_ns_list_log(self.fd, pdata)

    def nvme_effects_log(self, pdata):
        return self.driver.nvme_effects_log(self.fd, pdata)

    def nvme_self_test_log(self, pdata):
        return self.driver.nvme_self_test_log(self.fd, pdata)

    def nvme_get_telemetry_log(self, generate_report, ctrl_init, log_page_size, offset, pdata):
        return self.driver.nvme_get_telemetry_log(self.fd, pdata, generate_report, ctrl_init, log_page_size, offset)

    def nvme_sanitize_log(self, pdata):
        return self.driver.nvme_sanitize_log(self.fd, pdata)

    def nvme_subsystem_reset(self):
        return self.driver.nvme_subsystem_reset(self.fd)

    def nvme_reset_controller(self):
        return self.driver.nvme_reset_controller(self.fd)

    def nvme_ns_create(self, nsze, ncap, flbas, dps, nmic, timeout, presult):
        return self.driver.nvme_ns_create(self.fd, nsze, ncap, flbas, dps, nmic, timeout, presult)

    def nvme_ns_delete(self, nsid, timeout):
        return self.driver.nvme_ns_delete(self.fd, nsid, timeout)

    def nvme_ns_attach_ctrls(self, nsid, num_ctrls, pctrlist):
        return self.driver.nvme_ns_attach_ctrls(self.fd, nsid, num_ctrls, pctrlist)

    def nvme_ns_detach_ctrls(self, nsid, num_ctrls, pctrlist):
        return self.driver.nvme_ns_detach_ctrls(self.fd, nsid, num_ctrls, pctrlist)




nv = NVMe()
nv.nvme_reset_controller()