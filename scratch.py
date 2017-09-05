
import datetime
from datetime import date

def process_dates(start_date, end_date):

    range_year = end_date.year - start_date.year + 1
    range_month = end_date.month - start_date.month + 1
    months_to_process = range_year * 12 + range_month




process_dates(date(2017, 8, 31), date(2018, 9, 1))


