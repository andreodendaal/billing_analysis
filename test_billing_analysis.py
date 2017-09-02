import workday_calc as workdays
import billable_hours as billhrs
import unittest
from datetime import date


class TestAdd(unittest.TestCase):

    def test_file_processing(self):
        ref_dict = {'Ian Cabacov': {'un_billable_hours': 48.0, 'billable_hours': 9.5}, 'John Hobeica': {'un_billable_hours': 10.5, 'billable_hours': 39.0}, 'Ion Cotoros': {'un_billable_hours': 22.5, 'billable_hours': 18.0}}
        self.assertDictEqual(ref_dict, billhrs.process_hours('test_hours.csv'))

    def test_workday_calc(self):

        self.assertEqual(workdays.workdays_calc(date(2017, 8, 25), date(2017, 8, 26)), 1)
        self.assertEqual(workdays.workdays_calc(date(2017, 8, 28), date(2017, 9, 4), [date(2017, 9, 4)]), 5)


