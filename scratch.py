
import datetime
from datetime import date

def process_dates(start_date, end_date):

    date_range_year = end_date.year - start_date.year + 1
    print(date_range_year)
    date_range_month = end_date.month - start_date.month + 1
    print(date_range_month)
    months_to_process = date_range_year * 12 + date_range_month
    print(months_to_process)

process_dates(date(2017, 8, 31), date(2018, 9, 1))


