
import pandas as pd
from datetime import datetime,timedelta

def get_disabled_days(reservations):
    disabled_days = []
    for reservation in reservations:
        date_range_pd = pd.date_range(reservation.start_date, reservation.end_date - timedelta(days=1), freq='d')
        for day in date_range_pd:

            disabled_days.append(datetime.strftime(day, '%y-%m-%d'))
    return disabled_days


def raw_date_handler(raw_dates):

    check_in = raw_dates[0]
    check_in_first = check_in.split('.')[0]
    check_in_second = check_in.split('.')[1]
    check_in_third = check_in.split('.')[2]
    formatted_checkin = check_in_third + "-" + check_in_second + "-" + check_in_first

    check_out = raw_dates[1]
    check_out_first = check_out.split('.')[0]
    check_out_second = check_out.split('.')[1]
    check_out_third = check_out.split('.')[2]
    formatted_checkout = check_out_third + "-" + check_out_second + "-" + check_out_first

    datetime_check_in = datetime.strptime(formatted_checkin, '%Y-%m-%d')
    datetime_check_out = datetime.strptime(formatted_checkout, '%Y-%m-%d')

    return datetime_check_in,datetime_check_out

def get_total_price(datetime_check_in,datetime_check_out,price_intervals,villa):
    delta = timedelta(days=1)
    total_price = 0
    while datetime_check_in < datetime_check_out:
        price_day = price_intervals.filter(start_date__lte=datetime_check_in, end_date__gte=datetime_check_in)
        datetime_check_in += delta
        if len(price_day) != 0:
            total_price += price_day[0].price
        else:
            total_price += villa.default_price
    return total_price