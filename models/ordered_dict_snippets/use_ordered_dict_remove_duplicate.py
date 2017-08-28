# coding: utf-8
from collections import OrderedDict


def remove_duplicate(items):
    print("=== remove_duplicate ===")
    return list(OrderedDict.fromkeys(items))


def main():
    ids = [1, 3, 4, 1, 2, 3]
    print(remove_duplicate(ids))


if __name__ == '__main__':
    main()
