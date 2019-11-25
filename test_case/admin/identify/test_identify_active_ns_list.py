import sys
sys.path.append("../../../")

from nose.tools import assert_equal, nottest, assert_raises
from lib.logic.nvme.admin.identify import *


class TestIdentifyActiveList(object):

    def __init__(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_print_identify(self):
        identify = IdentifyActiveNamespaceList()
        identify.printf()

    def test_namespace_1_list(self):
        identify = IdentifyActiveNamespaceList()
        active_namespace_list = identify.identify_data
        identify_result = identify.identify_result
        ns_id = 1
        ns_item = active_namespace_list[ns_id-1]
        assert_equal(ns_item, 0x1, msg="namespace 1, active list item should same as 1, but it is {}".format(ns_item))
        assert_equal(identify_result, 0x0, msg="identify_result expect 0, but it is {}".format(identify_result))


