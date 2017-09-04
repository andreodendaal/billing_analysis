from datetime import timedelta
from datetime import date
import calendar

def slice_year_month(start_date, end_date):
    '''

    :param start_date:
    :param end_date:
    :return: dict, int
    Take Date range and slice it into year/month and days in each month
    if start and end date are not on the beginning or end of the month the funtion
    calculates slice for that month
    return:
        dictionary:
            d_sliceby_year_month{YYYY_MM:{'Month':{'num_days: 00}}}
        int
            total_days_in_slice

    '''

    # build dictionary
    d_sliceby_year_month = {}
    total_days_in_slice = 0

    range_year = end_date.year - start_date.year
    range_months_edges = end_date.month - start_date.month + 1

    if range_year == 0:
        months_to_process = range_months_edges
    else:
        months_to_process = range_year * 12 + range_months_edges


    year_link = start_date.year
    month_num = start_date.month

    for ctr in range(months_to_process):

        end_of_month = calendar.monthrange(year_link, month_num)[1]
        name_ofmonth = calendar.month_name[month_num]

        month_detail = {}

        date_to = date(year_link, month_num, end_of_month)
        # Process first month
        if ctr == 0:
            date_from = start_date
            month_detail['num_days'] = end_of_month - (start_date.day - 1)
            date_to = date(year_link, month_num, end_of_month)
        # Process last month
        elif ctr == months_to_process - 1:
            date_to = end_date
        # add sliced days
            month_detail['num_days'] = end_date.day

        # Process full Months
        else:
            date_from = date(year_link, month_num, 1)
            month_detail['num_days'] = end_of_month

        total_days_in_slice = total_days_in_slice + month_detail['num_days']

        month_days = {}

        month_days[name_ofmonth] = month_detail

        month_detail['date_range'] = [date_from, date_to]

        slice_key = str(year_link) + '_' + str(month_num)

        d_sliceby_year_month[slice_key] = month_days
        month_num += 1

        if month_num == 13:
            year_link += 1
            month_num = 1

        # print(date_from)
        # print(date_to)
        # print(month_detail['num_days'])
        # print(total_days_in_slice)

    print(total_days_in_slice)

    return d_sliceby_year_month, total_days_in_slice

if __name__ == '__main__':

    print(slice_year_month(date(2017, 12, 1), date(2018, 1, 31)))
