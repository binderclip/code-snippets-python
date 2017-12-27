# coding: utf-8
from gevent import monkey; monkey.patch_sys()
import gevent
# import time


def f(n):
    # time.sleep(0.01)
    for i in range(n):
        print gevent.getcurrent(), i
    # 是失败的


def main():
    g1 = gevent.spawn(f, 5)
    g2 = gevent.spawn(f, 5)
    g3 = gevent.spawn(f, 5)
    gevent.joinall([g1, g2, g3])


if __name__ == '__main__':
    main()



