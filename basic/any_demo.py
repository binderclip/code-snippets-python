# coding: utf-8


def c1():
    print('c1')
    return True


def c2():
    print('c2')
    return False


def main():
    print(any([c1(), c2()]))
    if c1() or c2():
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()
