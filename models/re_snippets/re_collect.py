# coding: utf-8
import re


def find_and_print(order, r, s, group=0):
    m = re.search(r, s)
    print('{}: {} | {}'.format(order, s, m.group(group) if m else None))


def main():
    s = '- [1.1.1 连接管理与安全性](#1.1.1 连接管理与安全性)'   # to find 1.1.1 连接管理与安全性
    find_and_print('A', r"\(#(.*)\)", s, 1)
    r_url = r"^(ht|f)tp(s?)\:\/\/[0-9a-zA-Z]([-.\w]*[0-9a-zA-Z])*(:(0-9)*‌​)*(\/?)([a-zA-Z0-9\-‌​\.\?\,\'\/\\\+&amp;%‌​\$#_]*)?$"
    s = 'xxx http://exp.com'    # to find None
    find_and_print('B', r_url, s, 0)
    s = 'http://exp.com'        # to find http://exp.com
    find_and_print('B', r_url, s, 0)


if __name__ == '__main__':
    main()

# https://stackoverflow.com/questions/161738/what-is-the-best-regular-expression-to-check-if-a-string-is-a-valid-url
