from datetime import datetime, timedelta

weekends = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


def get_previous_dayday(dayname, start_date=None):
    """获得当天上一周的某天日期"""
    if start_date is None:
        start_date = datetime.now()  # 从当前日期计数上一周
    date_start = start_date.weekday()
    date_end = weekends.index(dayname)  # 获取星期的索引
    days_ago = (7+date_start-date_end) % 7
    if days_ago == 0:
        days_ago = 7
    return start_date - timedelta(days=days_ago)


if __name__ == '__main__':
    res = get_previous_dayday('Sunday')
    print(res)
    res2 = get_previous_dayday('Sunday', datetime(2020, 6, 10))
    print(res2)
