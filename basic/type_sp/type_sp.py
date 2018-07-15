class Foo:
    """hello foo"""
    pass


def main():
    print(type(1))
    print(type(3.3))
    print(type('s'))
    print(type(object()))
    print(type(object))
    print(type(int))
    print(type(Foo()))
    print(type(Foo))
    print('===')
    print(Foo.__name__)
    print(Foo.__class__)
    print(Foo.__doc__)


if __name__ == '__main__':
    main()
