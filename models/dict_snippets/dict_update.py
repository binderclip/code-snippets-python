# coding: utf-8


def main():
    d = {}
    print(d)
    d['a'] = 'aa'
    d.update(b='bb')
    print(d)
    d.pop('a')
    print(d)
    print(d.popitem())
    print(d)
    d = {
        'c': 'cc',
        'd': 'dd',
    }
    print(d)
    d.clear()
    print(d)


if __name__ == '__main__':
    main()
