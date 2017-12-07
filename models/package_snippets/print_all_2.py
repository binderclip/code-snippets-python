# coding: utf-8
from test_all import *


def main():
    print('a: {}'.format(a))
    print('b: {}'.format(b))
    # print('c: {}'.format(c))    # NameError: global name 'c' is not defined
    # print('all_a_a: {}'.format(all_a_a))    # NameError: global name 'all_a_a' is not defined


if __name__ == '__main__':
    main()
