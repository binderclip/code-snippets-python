import math
import datetime


def datetime_range(start_time, end_time):
    return [start_time + datetime.timedelta(hours=x) for x in range(math.ceil((end_time - start_time).total_seconds() / 3600))]


def datetime_pairs(start_time, end_time):
    dts = datetime_range(start_time, end_time)
    for i, dt in enumerate(dts):
        yield dt, dts[i + 1] if i + 1 < len(dts) else end_time


def main():
    start_time = datetime.datetime(2018, 3, 28, 22)
    end_time = datetime.datetime(2018, 3, 29, 0, 30)

    print(datetime_range(start_time, end_time))
    print(list(datetime_pairs(start_time, end_time)))


if __name__ == '__main__':
    main()
