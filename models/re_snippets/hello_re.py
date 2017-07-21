# coding: utf-8
import re


def search_hello(s):
    m = re.search('hello', s)
    if m:
        print(m.group())
    else:
        print('not found')


def main():
    search_hello('hello world')
    search_hello('hi world')

if __name__ == '__main__':
    main()
