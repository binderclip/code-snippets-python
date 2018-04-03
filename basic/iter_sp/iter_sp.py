def func(i: int):
    for i in range(i, i + 2):
        yield i * i


def iter_print(it):
    print(f'>>> {it}:')
    for i in it:
        print(i)


def main():
    l = ['foo', 'bar']
    s = {'a', 'b'}
    r = range(3)
    f = func(2)
    print(l, s, r, f)
    print(iter(l), iter(s), iter(r), iter(f))

    for x in (l, s, r, f):
        iter_print(x)

    print(iter(iter(l)))
    print(iter(iter(iter(l))))

    # raise some exceptions
    # iter(1)     # TypeError: 'int' object is not iterable
    # list(1)     # TypeError: 'int' object is not iterable


if __name__ == '__main__':
    main()

# https://docs.python.org/3/tutorial/classes.html#iterators
