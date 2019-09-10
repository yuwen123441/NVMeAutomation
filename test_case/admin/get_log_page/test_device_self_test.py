import sys
sys.path.append("../../../")
from lib.logic.nvme.admin.get_log_page import DeviceSelfTest
from nose.tools import assert_equal, assert_in, assert_raises


class TestDeviceSelfTest(object):
    """
    Log Identifier 06h
    """

    def __init__(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_printf(self):
        self_test_log = DeviceSelfTest()
        self_test_log.printf()
        assert_equal(self_test_log.get_log_page_result, 0)
