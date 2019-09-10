import sys
sys.path.append("../../../")

from nose.tools import assert_equal, nottest, assert_raises
from lib.logic.nvme.admin.identify import *


class TestIdentifyNSDescriptorList(object):

    def __init__(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_print_namespace(self):
        identify = IdentifyDescriptorList()
        identify.printf()