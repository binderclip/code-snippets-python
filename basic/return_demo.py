# coding: utf-8


def f_a():
    return


def f_b():
    return 1, 2


def main():
    # foo, bar = f_a()  # TypeError: 'NoneType' object is not iterable
    foo, bar = f_b()
    print(foo, bar)


if __name__ == '__main__':
    main()
