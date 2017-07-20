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


class Foo(object):

    @timeit
    def foo(self, a=2, b=3):
        time.sleep(0.2)


@timeit
def f1():
    time.sleep(1)
    print 'f1'


@timeit
def f2(a):
    time.sleep(2)
    print 'f2', a


@timeit
def f3(a, *args, **kw):
    time.sleep(0.3)
    print 'f3', args, kw


def main():
    f1()
    f2(42)
    f3(42, 43, foo=2)
    Foo().foo()


if __name__ == '__main__':
    main()


# ref: https://www.andreas-jung.com/contents/a-python-decorator-for-measuring-the-execution-time-of-methods