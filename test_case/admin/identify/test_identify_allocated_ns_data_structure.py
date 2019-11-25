import sys
sys.path.append("../../../")

from nose.tools import assert_equal, nottest, assert_raises, assert_not_equal
from lib.logic.nvme.admin.identify import *


class TestAllocatedNSDataStructure(object):

    def __init__(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_printf(self):
        identify = IdentifyAllocatedNamespace(nsid=1)
        identify.printf()

    def test_allocated_ns(self):
        identify = IdentifyAllocatedNamespace(nsid=1)
        assert_equal(identify.identify_result, 0, msg="nsid = 0x1 is valid, identify should succeed")

    def test_invalid_ns(self):
        identify = IdentifyAllocatedNamespace(nsid=0x10)
        assert_not_equal(identify.identify_result, 0, msg="nsid = 0x10 is invalid, identify should failed")


    def test_ns_0xffffffff(self):
        identify = IdentifyAllocatedNamespace(nsid=0xffffffff)
        assert_not_equal(identify.identify_result, 0, msg="nsid = 0xffffffff is invalid, identify should failed")
