import sys
sys.path.append("../../../")

from nose.tools import assert_equal, nottest, assert_raises
from lib.logic.nvme.admin.identify import *



class TestIdentifyNamespace(object):

    def __init__(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_print_namespace(self):
        identify = IdentifyNamespace(nsid=1)
        identify.printf()

    def test_ncap(self):
        identify = IdentifyNamespace(nsid=1)
        ncap = identify.identify_data.ncap
        assert_equal(ncap, 1875385008, msg="ncap should same as 1875385008, but it is {}".format(ncap))
        assert_equal(identify.identify_result, 0, msg="result expect 0, but it is {}".format(identify.identify_result))