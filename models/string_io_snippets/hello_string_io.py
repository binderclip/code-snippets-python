# coding: utf-8
from StringIO import StringIO


def main():
    text = 'hello world!'
    temp = StringIO()
    temp.write(text)
    temp.seek(0)
    temp.name = 'hello.txt'
    print(temp)
    print(temp.name)
    print(temp.read())
    temp.close()


if __name__ == '__main__':
    main()
