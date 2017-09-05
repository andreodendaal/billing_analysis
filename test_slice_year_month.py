import slice_year_month as slice
import unittest
from datetime import date


class TestSlice(unittest.TestCase):

    def test_slice_year_month(self):
        ref_dict = {'2017_8': {'August': {'num_days': 31, 'date_range': [date(2017, 8, 1), date(2017, 8, 31)]}}}
        function_dict, function_total = slice.slice_year_month(date(2017, 8, 1), date(2017, 8, 31))
        self.assertDictEqual(ref_dict, function_dict)
        self.assertEqual(function_total, 31)

        ref_dict = {'2017_12': {'December': {'num_days': 31, 'date_range': [date(2017, 12, 1), date(2017, 12, 31)]}}, '2018_1': {'January': {'num_days': 31, 'date_range': [date(2017, 12, 1), date(2018, 1, 31)]}}}
        function_dict, function_total = slice.slice_year_month(date(2017, 12, 1), date(2018, 1, 31))
        self.assertDictEqual(ref_dict, function_dict)
        self.assertEqual(function_total, 62)

        function_dict, function_total = slice.slice_year_month(date(2017, 1, 1), date(2017, 12, 31))
        self.assertEqual(function_total, 365)

        function_dict, function_total = slice.slice_year_month(date(2017, 1, 1), date(2017, 2, 1))
        self.assertEqual(function_total, 32)

        # Test Leap year
        function_dict, function_total = slice.slice_year_month(date(2020, 2, 1), date(2020, 3, 31))
        self.assertEqual(function_total, 60)

        function_dict, function_total = slice.slice_year_month(date(2020, 1, 1), date(2020, 12, 31))
        self.assertEqual(function_total, 366)

        function_dict, function_total = slice.slice_year_month(date(2020, 1, 1), date(2021, 1, 1))
        self.assertEqual(function_total, 367)

