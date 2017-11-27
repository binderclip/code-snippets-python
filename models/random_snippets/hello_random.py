# coding: utf-8
import random


def test_randrange():
    print('=== test_randrange ===')
    s = ''
    for i in xrange(100):
        s += '{} '.format(random.randrange(5))
    print(s)

    s = ''
    for i in xrange(100):
        s += '{} '.format(random.randrange(start=1, stop=3, step=1))
    print(s)


def test_sample():
    print('=== test_sample ===')
    l = range(1, 5)
    s = ''
    for i in xrange(100):
        s += '{} '.format(random.sample(l, 2))
    print s


def main():
    test_randrange()
    test_sample()


if __name__ == '__main__':
    main()
