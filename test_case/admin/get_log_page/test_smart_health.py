

import sys
sys.path.append("../../../")
from lib.logic.nvme.admin.get_log_page import SmartHealthInformation
from nose.tools import assert_equal, assert_in, assert_raises, assert_true


class TestSmartHealth(object):

    def __init__(self):
        self.smart_health_information = SmartHealthInformation(nsid=1)

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_printf(self):
        self.smart_health_information.printf()
        assert_equal(self.smart_health_information.get_log_page_result, 0)

    def test_available_spare(self):
        assert_in(self.smart_health_information.log_page_data.aspare, range(0, 100))

    def test_composite_temperature(self):
        temperature_range = range(270, 363)  # set temperature range 1 ~ 60
        temp = self.smart_health_information.log_page_data.ct
        assert_in(temp, temperature_range, msg='temperature is not in range 30 ~ 90')

    def test_available_spare_threshold(self):
        asparet_range = range(0, 100)
        temp = self.smart_health_information.log_page_data
        assert_in(temp.asparet, asparet_range, msg='available_spare threshold: %s not in range 0 ~ 100'%temp.asparet)

    def test_percentage_used(self):
        percentage_used_range = range(0, 255)
        temp = self.smart_health_information.log_page_data
        assert_in(temp.prctu, percentage_used_range, msg='percentage_used: %s is not in range 1 ~ 99'%temp.prctu)

    def test_error_info_log_entries(self):
        "test_number_of_error_information_log_entries"
        temp = self.smart_health_information.log_page_data
        neile = buf.generate_big_number(temp.neile)
        assert_true(neile >= 0, msg='number_of_error_information_log_entries failed')

    def test_warning_temp_time(self):
        "test_warning_composite_temperature_time"
        temp = self.smart_health_information.log_page_data
        wctt = temp.wctt
        assert_true(wctt >= 0, msg='test_warning_composite_temperature_time failed')

    def test_critical_temp_time(self):
        "test_critical_composite_temperature_time"
        temp = self.smart_health_information.log_page_data
        cctt = temp.cctt
        assert_true(cctt >= 0, msg='test_warning_composite_temperature_time failed')

    def test_critical_temp_s1(self):
        "Temperature Sensor 1"
        temp = self.smart_health_information.log_page_data
        ts1 = temp.ts1
        assert_true(ts1 >= 0, msg='test_temperature_sensor1 failed')

    def test_critical_temp_s2(self):
        "Temperature Sensor 2"
        temp = self.smart_health_information.log_page_data
        temps = temp.ts2
        assert_true(temps >= 0, msg='test_temperature_sensor2 failed')

    def test_critical_temp_s3(self):
        "Temperature Sensor 3"
        temp = self.smart_health_information.log_page_data
        temps = temp.ts3
        assert_true(temps >= 0, msg='test_temperature_sensor2 failed')

    def test_critical_temp_s4(self):
        "Temperature Sensor 4"
        temp = self.smart_health_information.log_page_data
        temps = temp.ts4
        assert_true(temps >= 0, msg='test_temperature_sensor2 failed')

    def test_critical_temp_s5(self):
        "Temperature Sensor 5"
        temp = self.smart_health_information.log_page_data
        temps = temp.ts5
        assert_true(temps >= 0, msg='test_temperature_sensor2 failed')

    def test_critical_temp_s6(self):
        "Temperature Sensor 6"
        temp = self.smart_health_information.log_page_data
        temps = temp.ts6
        assert_true(temps >= 0, msg='test_temperature_sensor2 failed')

    def test_critical_temp_s7(self):
        "Temperature Sensor 7"
        temp = self.smart_health_information.log_page_data
        temps = temp.ts7
        assert_true(temps >= 0, msg='test_temperature_sensor2 failed')

    def test_critical_temp_s8(self):
        "Temperature Sensor 8"
        temp = self.smart_health_information.log_page_data
        temps = temp.ts8
        assert_true(temps >= 0, msg='test_temperature_sensor2 failegd')