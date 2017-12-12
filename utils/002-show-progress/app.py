# coding: utf-8
import sys
import time


def main():
    print('=== start ===')
    n = 15
    l = range(n)
    for i, _ in enumerate(l):
        sys.stdout.write('\r{}/{} ({:.2f}%)'.format(i + 1, n, 100.0 * (i + 1) / n))
        time.sleep(0.1)
    print('\n=== end ===')


if __name__ == '__main__':
    main()
