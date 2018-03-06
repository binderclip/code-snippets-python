# coding: utf-8


def main():
    import foo
    print('__name__: {}'.format(__name__))
    print('foo: {}'.format(foo))
    print('foo.print_foo: {}'.format(foo.print_foo))
    # print('foo.foo_a: {}'.format(foo.foo_a))  # AttributeError: 'module' object has no attribute 'foo_a'


def main2():
    import foo.foo_a
    print('foo: {}'.format(foo))
    print('foo.foo_a: {}'.format(foo.foo_a))


if __name__ == '__main__':
    main()
    main2()
