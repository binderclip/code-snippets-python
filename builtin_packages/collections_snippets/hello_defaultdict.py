# coding: utf-8
from collections import defaultdict


def main():
    print(int(), int())
    dd = defaultdict(int)
    print(dd['a'], dd['b'])

    print(str(), str())
    dd = defaultdict(str, {'a': 'aa'})
    print(dd['a'], dd['b'])

    print(bool(), bool())
    dd = defaultdict(bool)
    print(dd['a'], dd['b'])

    dd = defaultdict(lambda: 3)
    print(dd['a'], dd['b'])

    dd = defaultdict(lambda: [])
    print(dd['a'], dd['b'])


if __name__ == '__main__':
    main()
