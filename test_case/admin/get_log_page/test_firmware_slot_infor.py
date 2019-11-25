
import sys
sys.path.append("../../../")
from lib.logic.nvme.admin.get_log_page import FirmwareSlotInformation
from nose.tools import assert_equal, assert_in, assert_raises


class TestFWSlotInformation(object):

    def __init__(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_printf(self):
        fw_slot = FirmwareSlotInformation()
        fw_slot.printf()
        assert_equal(fw_slot.get_log_page_result, 0)