# coding: utf-8
from __future__ import print_function
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def main():
    sys.stderr.write('spam\n')
    print('spam', file=sys.stderr)
    eprint('spam')


if __name__ == '__main__':
    main()


# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
