import time
import datetime


def dt2ts():
    print("=== dt2ts ===")
    dt = datetime.datetime.now()
    print(dt.timestamp())   # python 2 中没有这个方法
    print(time.time())

    d = datetime.datetime.now().date()
    print(d)
    print(datetime.datetime.combine(d, datetime.time()).timestamp())
    print(time.mktime(d.timetuple()))


def ts2dt():
    print("=== ts2dt ===")
    ts = 1575266499
    dt = datetime.datetime.fromtimestamp(ts)
    print(dt)


def main():
    dt2ts()
    ts2dt()


if __name__ == '__main__':
    main()

#  https://www.programiz.com/python-programming/datetime/timestamp-datetime
