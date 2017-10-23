# coding: utf-8


def main():
    print(range(0))
    print(range(1))
    print(range(0, 1))
    print(range(0, 1, 1))
    print(range(10, 15, 4))
    print(range(-2))
    print(range(0, -2, -1))
    print(xrange(0, -2, -1))
    print(list(xrange(0, -2, -1)))


if __name__ == '__main__':
    main()


# https://docs.python.org/2/library/functions.html#range
# https://docs.python.org/2/library/functions.html#xrange
