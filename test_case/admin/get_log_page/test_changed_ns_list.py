import sys
sys.path.append("../../../")
from lib.logic.nvme.admin.get_log_page import ChangedNSList
from nose.tools import assert_equal, assert_in, assert_raises


class TestChangedNSList(object):

    def __init__(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_printf(self):
        change_list = ChangedNSList()
        change_list.printf()
        assert_equal(change_list.get_log_page_result, 0, msg="Get log page: get changed ns list failed")