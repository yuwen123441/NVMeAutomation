import sys
sys.path.append("../../../")

from nose.tools import assert_equal, nottest, assert_raises
from lib.logic.nvme.admin.identify import *


class TestIdentifyAllocatedNSList(object):

    def __init__(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_print_identify(self):
        identify = IdentifyAllocatedNamespaceList()
        identify.printf()

    def test_namespace_1_list(self):
        identify = IdentifyAllocatedNamespaceList()
        allocated_namespace_list = identify.identify_data
        ns_id = 1
        ns_item = allocated_namespace_list[ns_id-1]
        assert_equal(ns_item, 0x1, msg="ns 1 expect 1, but it is {} or not enable multi-namespace".format(ns_item))
        assert_equal(identify.identify_result, 0x0, msg="identify_result expect 0, but it is {}".format(ns_item))
