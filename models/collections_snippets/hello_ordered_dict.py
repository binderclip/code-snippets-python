# coding: utf-8
from collections import OrderedDict


def main():
    d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
    print(d)
    od = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
    print(od)
    print(od['banana'])
    od['grape'] = 10
    print(od)

    # print(od[0])    # KeyError: 0


if __name__ == '__main__':
    main()
