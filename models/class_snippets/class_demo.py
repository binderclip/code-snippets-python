# coding: utf-8


class A(object):

    def __init__(self):
        pass

    def hello(self):
        print('A: Hello')


class A2(A):

    def __init__(self):
        super(A2, self).__init__()

    def hello(self):
        super(A2, self).hello()
        print('A2: Hello')


def main():
    a = A()
    a.hello()
    a2 = A2()
    a2.hello()


if __name__ == '__main__':
    main()
