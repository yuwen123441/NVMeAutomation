import sys
sys.path.append("../../../")
from lib.logic.nvme.admin.get_log_page import SanitizeStatusLog
from nose.tools import assert_equal, assert_in, assert_raises


class TestSanitizeStatus(object):
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
        sanitize_status = SanitizeStatusLog()
        sanitize_status.printf()
        assert_equal(sanitize_status.get_log_page_result, 0)