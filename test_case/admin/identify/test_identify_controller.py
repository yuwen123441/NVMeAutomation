import sys
sys.path.append("../../../")

from nose.tools import assert_equal, nottest, assert_raises
from lib.logic.nvme.admin.identify import *



class TestIdentifyController(object):


    def __init__(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_print_identify_controller(self):
        identify = IdentifyController()
        identify.printf()

    def test_vid(self):
        identify = IdentifyController()
        vid = identify.identify_data.vid
        assert_equal(vid, 5284, msg="vid should same as 5284, but it is {}".format(vid))
        assert_equal(identify.identify_result, 0, msg="identify_result expect 0, but get {}".format(identify.identify_result))