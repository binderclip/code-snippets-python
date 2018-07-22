import re


def search_hello(s):
    m = re.search('hello', s)
    if m:
        print(m.group())
    else:
        print('not found')


def search_hello2(s):
    prog = re.compile('hello')
    m = prog.search(s)
    if m:
        print(m.group())
    else:
        print('not found')


def main():
    search_hello('hello world')
    search_hello('hi world')
    search_hello2('hello world')

if __name__ == '__main__':
    main()
