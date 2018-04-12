def identity(f):
    return f


@identity
def foo():
    return 'bar'


def main():
    print(foo())


if __name__ == '__main__':
    main()
