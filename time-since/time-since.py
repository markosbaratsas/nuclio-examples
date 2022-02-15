from datetime import datetime
from dateutil import relativedelta

def add_to_s(i, type_of_time, ret):
    if i == 1:
        ret += f"1 {type_of_time} "
    elif i > 1:
        ret += f"{str(i)} {type_of_time}s "
    return ret

def handler(context, event):
    try:
        date_str = str(event.body)
        date = datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')
    except:
        return "Please give the data in '%d/%m/%Y %H:%M:%S' format"

    now = datetime.now()
    diff = relativedelta.relativedelta(now, date)
    ret = ""

    ret = add_to_s(diff.years, "year", ret)
    ret = add_to_s(diff.months, "month", ret)
    ret = add_to_s(diff.days, "day", ret)
    ret = add_to_s(diff.hours, "hour", ret)
    ret = add_to_s(diff.minutes, "minute", ret)
    ret = add_to_s(diff.seconds, "second", ret)
    ret = ret[:-1]

    return str(ret)
