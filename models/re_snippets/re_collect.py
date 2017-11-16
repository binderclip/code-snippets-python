# coding: utf-8
import re


def find_and_print(order, r, s, group=0):
    m = re.search(r, s)
    print('{}: {} | {}'.format(order, s, m.group(group) if m else None))


def main():
    s = '- [1.1.1 连接管理与安全性](#1.1.1 连接管理与安全性)'   # to find 1.1.1 连接管理与安全性
    find_and_print('A', r"\(#(.*)\)", s, 1)


if __name__ == '__main__':
    main()
