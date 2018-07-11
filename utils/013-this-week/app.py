import datetime


def this_monday_and_related_sunday():
    now = datetime.datetime.now()
    today = datetime.datetime(now.year, now.month, now.day)
    this_monday = today - datetime.timedelta(now.weekday())
    related_sunday = this_monday + datetime.timedelta(6)
    return this_monday, related_sunday


def main():
    print(this_monday_and_related_sunday())


if __name__ == '__main__':
    main()
