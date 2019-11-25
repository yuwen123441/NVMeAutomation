import sys
sys.path.append("../../../")
from lib.logic.nvme.admin.get_log_page import CommandsSupportEffects
from nose.tools import assert_equal, assert_in, assert_raises


class TestCommandsSupportedEffects(object):

    def __init__(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_printf(self):
        commands = CommandsSupportEffects()
        commands.printf()
        assert_equal(commands.get_log_page_result, 0)