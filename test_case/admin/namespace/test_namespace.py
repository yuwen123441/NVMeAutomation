
import sys
sys.path.append("../../../")
from nose.tools import assert_equal, nottest, assert_raises
from lib.logic.nvme.admin.namespace import NameSpace


class TestNameSpace(object):


    def __init__(self):
        pass

    def test_create_namespace(self):
        control_list = [1]
        ns = NameSpace()
        ret = ns.create_namespace(1000,1000,1)
        print(ret)

        ret = ns.attach(control_list)
        print(ret)

        ret = ns.detach(control_list)



