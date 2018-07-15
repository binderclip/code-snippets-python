import inspect

from defines import Foo, foo


def main():
    print(inspect.getdoc(Foo))
    print(inspect.getsource(Foo))
    print(inspect.getsourcefile(Foo))
    print(inspect.getsourcelines(Foo))
    print(inspect.getcomments(Foo))
    print(inspect.getcomments(Foo.a))
    print(inspect.getcomments(Foo.bar))
    print(inspect.getcomments(foo))


if __name__ == '__main__':
    main()
