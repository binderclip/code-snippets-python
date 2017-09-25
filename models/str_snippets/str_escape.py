# coding: utf-8


def main():
    u = u'2017年'
    print(u)
    print(u.encode('unicode-escape'))
    print(repr(u.encode('unicode-escape')))
    print(u.encode('unicode-escape').encode('string-escape'))
    print(repr(u.encode('unicode-escape').encode('string-escape')))
    print(u.encode('unicode-escape').encode('string-escape').encode('string-escape'))
    print(repr(u.encode('unicode-escape').encode('string-escape').encode('string-escape')))
    print(u.encode('unicode-escape').encode('unicode-escape').encode('unicode-escape'))


if __name__ == '__main__':
    main()
