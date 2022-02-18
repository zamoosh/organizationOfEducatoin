import jdatetime
import datetime


def current_date():
    current = datetime.date.today()
    year, month, day = current.year, current.month, current.day
    j = jdatetime.date.fromgregorian(day=day, month=month, year=year, locale='fa_IR')
    day, month, year = j.day, j.month, j.year
    return year, month, day
