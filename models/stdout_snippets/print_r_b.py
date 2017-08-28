# coding: utf-8
import sys


def print_ver_d():
    print('=== print_ver_d ===')
    print 'Hello',      # print without newline in python 2
    print 'World'
    print 'A a',
    print '\b\bB bbb',
    print '\b' * 5,
    print 'C'


def stdout_ver_d():
    print('=== stdout_ver_d ===')
    sys.stdout.write('Hello ')
    sys.stdout.write('World')
    sys.stdout.write('\n')
    sys.stdout.write('A a')
    sys.stdout.write('\bB bbb')
    sys.stdout.write('\b' * 3)
    sys.stdout.write('C\n')
    sys.stdout.flush()


def print_ver_r():
    print('=== print_ver_r ===')
    print '    C',
    print '\r  B',
    print '\rA'


def stdout_ver_r():
    print('=== stdout_ver_r ===')
    sys.stdout.write('    C')
    sys.stdout.write('\r  B')
    sys.stdout.write('\rA\n')


def main():
    print_ver_d()
    stdout_ver_d()
    print_ver_r()
    stdout_ver_r()


if __name__ == '__main__':
    main()
