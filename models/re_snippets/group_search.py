# coding: utf-8
import re


def group_search():
    print('===== group_search =====')
    s = '"Foo" and "bar" are on the way.'
    m = re.search(r'"(.*)" and "(.*)" are on the way\.', s)
    if m:
        print('{} {}'.format(m.group(1), m.group(2)))
    else:
        print('not found')
    s = '"张三"和"李四"在路上。'
    m = re.search(r'"(.*)"和"(.*)"在路上。', s)
    if m:
        print('{} {}'.format(m.group(1), m.group(2)))
    else:
        print('not found')


def main():
    group_search()

if __name__ == '__main__':
    main()