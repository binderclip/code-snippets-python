# coding: utf-8


class A(object):
    def __init__(self, a):
        self.a = a

    def f1(self):
        print('hello f1')


def main():
    a1 = A('aaa')
    if hasattr(a1, 'f1'):
        a1.f1()
    if hasattr(a1, 'f2'):
        a1.f2()
    try:
        a1.f1()
    except AttributeError:
        pass
    try:
        a1.f2()
    except AttributeError:
        pass


if __name__ == '__main__':
    main()


# https://stackoverflow.com/questions/610883/how-to-know-if-an-object-has-an-attribute-in-python
