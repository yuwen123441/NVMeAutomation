import sys
sys.path.append("../../../")
from lib.logic.nvme.admin.get_log_page import TelemetryHostInitLog
from nose.tools import assert_equal, assert_in, assert_raises


class TestTelemetryHostInit(object):
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
        tel_host_init = TelemetryHostInitLog()
        tel_host_init.printf()
        assert_equal(tel_host_init.get_log_page_result, 0)