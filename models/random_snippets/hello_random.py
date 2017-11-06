# coding: utf-8
import random


def main():
    s = ''
    for i in xrange(100):
        s += '{} '.format(random.randrange(5))
    print(s)


if __name__ == '__main__':
    main()
