# coding: utf-8
import datetime


def _datetime(d):
    return datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')


def _strftime(d):
    return d.strftime('%Y-%m-%d %H:%M:%S')


def main():
    now = datetime.datetime.now()
    print(_strftime(now))
    t = _datetime("2017-09-03 17:37:48")
    print(t)


if __name__ == '__main__':
    main()
