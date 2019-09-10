

import sys
sys.path.append("../../../")
from lib.logic.nvme.admin.get_log_page import SmartHealthInformation
from nose.tools import assert_equal, assert_in, assert_raises


class TestSmartHealth(object):

    def __init__(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_printf(self):
        smart_health_information = SmartHealthInformation(nsid=1)
        smart_health_information.printf()
        assert_equal(smart_health_information.get_log_page_result, 0)

    def test_available_spare(self):
        smart_health_information = SmartHealthInformation(nsid=1)
        assert_in(smart_health_information.log_page_data.aspare, range(0, 100))