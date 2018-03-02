# coding: utf-8


class A(object):
    def __init__(self, a):
        self.a = a

    def f1(self):
        print('hello f1')


def main():
    a1 = A('aaa')
    print(A.__dict__)
    print(A.__dict__['f1'])
    print(hasattr(a1, 'f1'))
    print(hasattr(a1, 'f2'))
    a1.f1()
    # a1.f2()     # AttributeError: 'A' object has no attribute 'f2'

    d = {'b': 'bb'}
    # print(d.__dict__)   # AttributeError: 'dict' object has no attribute '__dict__'
    print(hasattr(d, 'b'))  # False
    print('b' in d)         # True


if __name__ == '__main__':
    main()


# https://stackoverflow.com/questions/610883/how-to-know-if-an-object-has-an-attribute-in-python
