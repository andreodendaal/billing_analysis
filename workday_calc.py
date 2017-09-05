from datetime import timedelta
from datetime import date
import calendar
import slice_year_month as slice

(MON, TUE, WED, THU, FRI, SAT, SUN) = range(7)


def workdays_calc(start_date, end_date, holidays=[], weekends=(SAT, SUN)):
    '''

    :param start_date: 
    :param end_date: 
    :param holidays: 
    :param weekends:     
    :return: dict

    '''

    delta_days = (end_date - start_date).days + 1

    full_weeks, extra_days = divmod(delta_days, 7)
    # num_workdays = how many days/week you work * total # of weeks
    num_workdays = (full_weeks + 1) * (7 - len(weekends))
    # subtract out any working days that fall in the 'shortened week'
    range_end = 8 - extra_days

    for d in range(1, range_end):

        time_delta = timedelta(d)
        enddate_timedelta = (end_date + time_delta)
        test = enddate_timedelta.weekday()

        if test not in weekends:
            num_workdays -= 1
    # skip holidays that fall on weekends
    holidays = [x for x in holidays if x.weekday() not in weekends]
    # subtract out any holidays
    for d in holidays:

        if start_date <= d <= end_date:
            num_workdays -= 1

    return num_workdays

def workdays_per_month(start_date, end_date, holidays=[]):
    '''
    :param date: 
    :param date: 
    :param list of date: 
    :return: dict
    
     Calculate the number of working days per month per country
     
    '''

    # slice date range into dictionary of year and months

    year_month_slices = {}

    year_month_slices['d'] = slice.slice_year_month(start_date, end_date)
    work_days = 28

    print((year_month_slices['d'][0]['2017_8']))
    print((year_month_slices['d'][0]['2017_8']['August']))
    print((year_month_slices['d'][0]['2017_8']['August']['num_days']))
    year_month_slices['d'][0]['2017_8']['August']['working_days'] = 10

    print((year_month_slices['d'][0]['2017_8']['August']))


    ctx = 0







    # add working days to dataset



    return


    # get working days per year month

    # build dictionary

    # return dictionary month: working_days

def get_workdays_by_country(start_date, end_date):

    pass
    # get dictionary of countries and holidays

    # build dictionary {country: {year_month : number of workdays}}


print(workdays_per_month(date(2017, 8, 15), date(2018, 9, 10)))