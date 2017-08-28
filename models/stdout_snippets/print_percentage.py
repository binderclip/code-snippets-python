# coding: utf-8
import sys
import time


def print_percentage(now, total):
    percentage = 100.0 * now / total
    sys.stdout.write('\r{}/{} {:.2f}%'.format(now, total, percentage) + ' ' * 20)
    sys.stdout.flush()


def print_percentage_end():
    sys.stdout.write("\n")
    sys.stdout.flush()


def test_print_percentage1():
    print("=== test_print_percentage1 ===")
    print_percentage(111, 100)
    time.sleep(0.5)
    print_percentage(2, 100)
    time.sleep(0.5)
    print_percentage(4, 100)
    time.sleep(0.5)
    print_percentage(10, 100)
    print_percentage_end()


def test_print_percentage2():
    print("=== test_print_percentage2 ===")
    total = 5
    for i in xrange(total):
        print_percentage(i + 1, total)
        time.sleep(0.5)
    print_percentage_end()


def main():
    test_print_percentage1()
    test_print_percentage2()


if __name__ == '__main__':
    main()


# https://stackoverflow.com/questions/3249524/print-in-one-line-dynamically
