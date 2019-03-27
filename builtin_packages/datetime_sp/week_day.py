import datetime


def this_monday_and_related_sunday():
    now = datetime.datetime.now()
    today = datetime.datetime(now.year, now.month, now.day)
    this_monday = today - datetime.timedelta(now.weekday())
    related_sunday = this_monday + datetime.timedelta(6)
    return this_monday, related_sunday


def chinese_weekday(dt: datetime.datetime) -> str:
    cn_number = ['一', '二', '三', '四', '五', '六', '日']
    return f'周{cn_number[dt.weekday()]}'


def main():
    print('Hello')
    dt = datetime.datetime(2019, 3, 25)
    print(dt, dt.weekday())  # 周一 0

    dt += datetime.timedelta(days=6)
    print(dt, dt.weekday())  # 周日 6

    this_monday, related_sunday = this_monday_and_related_sunday()
    print(chinese_weekday(this_monday), chinese_weekday(related_sunday))


if __name__ == '__main__':
    main()
