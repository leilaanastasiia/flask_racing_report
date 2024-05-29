from itertools import count
from typing import Any
from datetime import datetime

from database_app.models import Report


def str_to_datetime(time: str) -> datetime:
    """
    Convert time string to datetime format
    """
    str_time = datetime.strptime(time, '%Y-%m-%d_%H:%M:%S.%f')
    return str_time


def subtract_time(time_end, time_start) -> float:
    """
    Subtract two datatime objects
    """
    result = datetime.combine(time_end.date(), time_end.time()) - \
             datetime.combine(time_start.date(), time_start.time())
    return abs(result.total_seconds())


def get_time(abb: str, flag: str) -> datetime:
    """
    Search time by abbreviation for start & end, then return datetime object
    """
    if flag == 'start':
        return str_to_datetime(Report.get(Report.abbreviation == abb).start)
    elif flag == 'end':
        return str_to_datetime(Report.get(Report.abbreviation == abb).end)


def search_by_abb(abb: str) -> list[Any] | str:
    """
    Prepare info for given name(s) of rider(s) -> ['name', 'car', time]
    """
    abbs = [abb.abbreviation for abb in Report.select()]
    if abb in abbs:
        query = Report.get(Report.abbreviation == abb)
        start_time = get_time(query.abbreviation, flag='start')
        end_time = get_time(query.abbreviation, flag='end')
        circle_time = subtract_time(end_time, start_time)
        return_data = [query.name, query.car, circle_time]
        return return_data
    else:
        raise ValueError('No such name was found')


def built_report(flag: str) -> dict[str, Any]:
    """
    Prepare data for logic of all names of riders
    Flag is used for the sorting order (asc | desc)
    """
    abbs_list = [abb.abbreviation for abb in Report.select()]
    unsorted_list, return_value = [], {}
    counter = count(start=1)
    for abb in abbs_list:
        unsorted_list.append(search_by_abb(abb))  # search by abb
    if flag == 'asc':
        sorted_list = sorted(unsorted_list, key=lambda time: time[2])  # [[name, car, time]]
        for item in sorted_list:
            # {{index: {'name': name, 'car': car, 'time': time}}}
            return_value.update({str(next(counter)): {'name': item[0],
                                                      'car': item[1],
                                                      'time': item[2]}})
        return return_value
    elif flag == 'desc':
        sorted_list = sorted(unsorted_list, key=lambda time: time[2], reverse=True)  # [[name, car, time]]
        for item in sorted_list:
            # {{index: {'name': name, 'car': car, 'time': time}}}
            return_value.update({str(next(counter)): {'name': item[0],
                                                      'car': item[1],
                                                      'time': item[2]}})
        return return_value
    else:
        raise ValueError('Flag should be "asc" or "desc"')


def built_drivers_list(flag: str) -> dict[str, Any]:
    """
    Prepare data of names with ABB of all riders
    Flag is used for the sorting order (asc | desc)
    """
    return_value = {}
    add_link = 'http://127.0.0.1:5000/api/v1/report/drivers/'
    qparams = '/?format=json'
    counter = count(start=1)
    if flag == 'asc':
        data = [[data.name, data.abbreviation] for data in Report.select().order_by(Report.name)]
        for item in data:
            return_value.update({str(next(counter)): {'name': item[0],
                                                      'link': add_link + item[1] + qparams}})
        return return_value  # index, name, link
    elif flag == 'desc':
        data = [[data.name, data.abbreviation] for data in Report.select().order_by(Report.name.desc())]
        for item in data:
            return_value.update({str(next(counter)): {'name': item[0],
                                                      'link': add_link + item[1] + qparams}})
        return return_value  # index, name, link
    else:
        raise ValueError('Flag should be "asc" or "desc"')
