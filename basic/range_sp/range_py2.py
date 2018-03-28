# coding: utf-8


def print_range(r):
    print(list(r))


def main():
    print(range(0))
    print_range(range(1))
    print_range(range(0, 1))
    print_range(range(0, 1, 1))
    print_range(range(10, 15, 4))
    print_range(range(-2))
    print_range(range(0, -2, -1))


if __name__ == '__main__':
    main()


# https://docs.python.org/2/library/functions.html#range
# https://docs.python.org/2/library/functions.html#xrange
