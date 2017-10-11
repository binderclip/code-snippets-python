# coding: utf-8
import datetime


def main():
    time_delta = datetime.datetime(2017, 7, 17) - datetime.datetime(2017, 7, 20)
    time_delta2 = datetime.timedelta(days=1)
    print(time_delta)
    print(abs(time_delta))
    print(time_delta2)


if __name__ == '__main__':
    main()
