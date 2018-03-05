
class X(object):
    pass


def main():
    print(X.__dict__)
    x = X()
    print(x.__dict__)
    x.xx = 'xxx'
    print(x.__dict__)


if __name__ == '__main__':
    main()
