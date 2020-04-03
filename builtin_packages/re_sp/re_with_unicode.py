# coding: utf-8
import re


def search_bad(s):
    m = re.search(r'不好|有问题', s)
    if m:
        print(s)
    else:
        print('not found')


def search_bad_str():
    print('===== search_bad_str =====')
    s1 = '这个有问题'
    s2 = '这个不好用'
    s3 = '这个不太好用'
    s4 = '这个不是很好用'
    search_bad(s1)
    search_bad(s2)
    search_bad(s3)
    search_bad(s4)


def search_bad_unicode():
    print('===== search_bad_str =====')
    s1 = '这个有问题'
    s2 = '这个不好用'
    s3 = '这个不太好用'
    s4 = '这个不是很好用'
    search_bad(s1)
    search_bad(s2)
    search_bad(s3)
    search_bad(s4)


def search_utf8(s):
    m = re.search(r'第 (\d+)', s)
    if m:
        print(m.group(1))
    else:
        print('not found')


def main():
    search_bad_str()
    search_bad_unicode()
    search_utf8('abc 第 10')


if __name__ == '__main__':
    main()
