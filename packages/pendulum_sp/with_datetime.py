import datetime
import pendulum


def main():
    dt = datetime.datetime(2016, 8, 20, 1, 2, 3)
    dt = pendulum.instance(dt)
    print(dt)

    dt = datetime.datetime(2016, 8, 20, 1, 2, 3)
    dt = pendulum.instance(dt, 'Asia/Shanghai')
    print(dt)

    dt = datetime.datetime(
        year=dt.year,
        month=dt.month,
        day=dt.day,
        hour=dt.hour,
        minute=dt.minute,
        second=dt.second,
        microsecond=dt.microsecond,
    )
    print(dt)


if __name__ == '__main__':
    main()
