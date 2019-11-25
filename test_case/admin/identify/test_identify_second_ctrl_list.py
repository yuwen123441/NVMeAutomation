import sys
sys.path.append("../../../")

from nose.tools import assert_equal, nottest, assert_raises
from lib.logic.nvme.admin.identify import *


class TestIdentifySecondCtrlList(object):

    def __init__(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_print(self):
        identify = SecondaryCtrlList(nsid=1, cntid=0)
        identify.printf()
        assert_equal(identify.identify_result&0xfff, 0)
