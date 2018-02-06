# coding: utf-8


def main():
    print(int('1'))
    try:
        print(int('x1'))
    except ValueError as e:
        print(e)
    try:
        print(int('xx'))
    except ValueError as e:
        print(e)
    try:
        print(int(None))
    except TypeError as e:
        print(e)


if __name__ == '__main__':
    main()
