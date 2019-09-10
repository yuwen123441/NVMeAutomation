
import sys
sys.path.append("../../../")
from lib.logic.nvme.admin.get_log_page import ErrorInformation
from nose.tools import assert_equal, nottest, assert_raises


class TestErrorInformation(object):

    def __init__(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_printf(self):
        error_information = ErrorInformation(entries=1)
        error_information.printf()
        assert_equal(error_information.get_log_page_result, 0)