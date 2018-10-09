from collections import OrderedDict


def test_ordered_dict():
    print('=== test_ordered_dict ===')
    d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
    print(d)
    od = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
    print(od)
    print(od['banana'])

    od['grape'] = 10
    print(od)

    od['banana'] = 1
    print(od)

    print(od.keys())
    # print(od[0])    # KeyError: 0


def test_init_ordered_dict():
    print('=== test_init_ordered_dict ===')
    data = [('foo', 'fooo'), ('bar', 'baar')]
    od = OrderedDict(data)
    print(od)
    print(list(od.keys()))
    print(list(od.items()))


def test_append_ordered_dict():
    print('=== test_append_ordered_dict ===')
    od = OrderedDict()
    od['foo'] = 1
    od['bar'] = 1
    od['baz'] = 1
    od['foo'] = 2
    print(od)
    print(list(od.keys()))


def main():
    test_ordered_dict()
    test_init_ordered_dict()
    test_append_ordered_dict()


if __name__ == '__main__':
    main()
