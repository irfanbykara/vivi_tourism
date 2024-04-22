
import pandas as pd
from datetime import datetime,timedelta
from .consts import *

def get_disabled_days(reservations):
    disabled_days = []
    for reservation in reservations:
        date_range_pd = pd.date_range(reservation.start_date, reservation.end_date - timedelta(days=1), freq='d')
        for day in date_range_pd:

            disabled_days.append(datetime.strftime(day, '%y-%m-%d'))
    return disabled_days

def get_yatch_attributes(yatch):
    yacht_attributes = {
        "brand": yatch.brand,
        "model": yatch.model,
        "made_year": yatch.made_year,
        "renovation_year": yatch.renovation_year,
        "cruising_capacity": yatch.cruising_capacity,
        "capacity": yatch.capacity,
        "num_rooms": yatch.num_rooms,
        "boarding_passenger_capacity": yatch.boarding_passanger_capacity,
        "height": yatch.height,
        "cenova": yatch.cenova,
        "main_sail": yatch.main_sail,
        "num_engine": yatch.num_engine,
        "engine_type": yatch.engine_type,
        "fuel_cost": yatch.fuel_cost,
        "fuel_type": yatch.fuel_type,
        "yatch_material": yatch.yatch_material,
        "num_rudder": yatch.num_rudder,
        "daily_cruise_duration": yatch.daily_cruise_duration,
        "daily_ac_duration": yatch.daily_ac_duration,
        "engine_horse_power": yatch.engine_horse_power,
        "fuel_capacity": yatch.fuel_capacity,
        "waste_tank_capacity": yatch.waste_tank_capacity,
        "water_tank_capacity": yatch.water_tank_capacity,
        "hall_height": yatch.hall_height,
        "width": yatch.width,
        "water_draft": yatch.water_draft,
    }

    # Remove keys with None values
    yacht_attributes = {key: value for key, value in yacht_attributes.items() if value is not None}

    yatch_attributes_tr = {}
    for key,value in yacht_attributes.items():
        key_tr = yatch_attribute_mapping[key]
        yatch_attributes_tr[key_tr] = str(value)

    return yatch_attributes_tr


def raw_date_handler(raw_dates):

    check_in = raw_dates[0]
    check_in_first = check_in.split(' ')[0]
    check_in_second = str(turkish_month_dict[check_in.split(' ')[1]])
    check_in_third = check_in.split(' ')[2]
    formatted_checkin = check_in_third + "-" + check_in_second + "-" + check_in_first

    check_out = raw_dates[1]
    check_out_first = check_out.split(' ')[0]
    check_out_second = str(turkish_month_dict[check_out.split(' ')[1]])
    check_out_third = check_out.split(' ')[2]
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