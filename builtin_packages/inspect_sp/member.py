import inspect


class Foo:
    '''Just a foo class'''
    a = 'A'     # the a


def main():
    print(inspect.getmembers(Foo))
    print(inspect.getmembers(Foo()))


if __name__ == '__main__':
    main()
