# coding: utf-8
import time


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te - ts)
        return result

    return timed


@timeit
def f1():
    for i in range(100):
        l1 = range(100000)
        l2 = filter(lambda x: x % 2 == 0, l1)


@timeit
def f2():
    for i in range(100):
        l1 = range(100000)
        l2 = [x for x in l1 if x % 2 == 0]


def main():
    f1()
    f2()


if __name__ == '__main__':
    main()
