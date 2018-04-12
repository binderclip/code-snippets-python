_functions = {}


def register(f):
    global _functions
    _functions[f.__name__] = f
    return f


@register
def foo():
    return 'bar'


@register
def baz():
    return 'qux'


def main():
    print(_functions)
    print(_functions['foo']())
    print(_functions['baz']())


if __name__ == '__main__':
    main()
