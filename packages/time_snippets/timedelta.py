# coding: utf-8
import datetime
import time


def main():
    now1 = datetime.datetime.now()
    time.sleep(1.1)
    now2 = datetime.datetime.now()
    print(now2 - now1)
    past = now2 - datetime.timedelta(days=1, seconds=1, microseconds=1, milliseconds=1, minutes=1, hours=1, weeks=1)
    print(past)


if __name__ == '__main__':
    main()
