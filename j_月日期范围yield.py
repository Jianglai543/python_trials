from datetime import datetime, timedelta


def get_month_days(start, stop, step):
    while start < stop:
        yield start
        start += step


if __name__ == '__main__':
    for d in get_month_days(datetime(2020, 6, 12), datetime(2020, 6, 30), timedelta(hours=12)):
        print(d)
