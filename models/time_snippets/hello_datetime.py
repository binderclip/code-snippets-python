# coding: utf-8
import datetime


def main():
    time_delta = datetime.datetime(2017, 7, 17) - datetime.datetime(2017, 7, 20)
    print(time_delta)
    print(abs(time_delta))


if __name__ == '__main__':
    main()
