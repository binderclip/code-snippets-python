# coding: utf-8
import sys
import time


def show_progress(p, n):
    sys.stdout.write('\r{}/{} ({:.2%})'.format(p, n, p / n))


def main():
    print('=== start ===')
    n = 15
    l = range(n)
    for i, _ in enumerate(l):
        show_progress(i + 1, n)
        time.sleep(0.1)
    print('\n=== end ===')


if __name__ == '__main__':
    main()
