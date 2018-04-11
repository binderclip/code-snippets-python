# coding: utf-8

def to_utf8(s):
    if isinstance(s, unicode):
        return s.encode('utf-8')
    return s


def to_unicode(s):
    if isinstance(s, str):
        return s.decode('utf-8')
    return s


def main():
    print(to_utf8('哈哈哈'), to_unicode('哈哈哈'))
    print(to_utf8(u'哈哈哈'), to_unicode(u'哈哈哈'))


if __name__ == '__main__':
    main()
