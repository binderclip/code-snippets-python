# coding: utf-8


def my_range(n):
    for i in xrange(0, n):
        yield i


def main():
    print('type: {}, {}'.format(type(my_range(2)), my_range(2)))
    print('type: {}, {}'.format(type(list(my_range(2))), list(my_range(2))))
    # print(len(my_range(2)))     # TypeError: object of type 'generator' has no len()
    # print(my_range(2)[0])   # TypeError: 'generator' object has no attribute '__getitem__'


if __name__ == '__main__':
    main()
