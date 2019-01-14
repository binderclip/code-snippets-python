# coding: utf-8
from collections import OrderedDict


def remove_duplicate1():
    print("=== remove_duplicate1 ===")
    ids = [1, 3, 4, 1, 2, 3]
    print(list(OrderedDict.fromkeys(ids)))


def remove_duplicate2():
    print("=== remove_duplicate2 ===")

    od = OrderedDict([(1, 'a'), (2, 'b'), (1, 'a')])
    print([v for _, v in od.items()])
    # return list(OrderedDict.fromkeys(items))


def main():
    remove_duplicate1()
    remove_duplicate2()


if __name__ == '__main__':
    main()
