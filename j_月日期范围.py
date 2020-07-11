from datetime import date, timedelta
import calendar


def get_month_days(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days)
    return (start_date, end_date)


if __name__ == '__main__':
    start, end = get_month_days()
    aday = timedelta(days=1)
    while start < end:
        print(start)
        start += aday
