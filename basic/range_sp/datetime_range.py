import datetime


def main():
    dts = range(datetime.datetime(2018, 3, 28), datetime.datetime(2018, 3, 29), datetime.timedelta(hours=1))
    print(dts)
    print('Hello')


if __name__ == '__main__':
    main()
