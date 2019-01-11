import time
import datetime


def main():
    dt = datetime.datetime.now()
    print(dt.timestamp())   # python 2 中没有这个方法
    print(time.time())

    d = datetime.datetime.now().date()
    print(d)
    print(datetime.datetime.combine(d, datetime.time()).timestamp())
    print(time.mktime(d.timetuple()))


if __name__ == '__main__':
    main()
