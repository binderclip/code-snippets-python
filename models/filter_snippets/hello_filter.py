# coding: utf-8


def main():
    a = ['a', None, 0, '', 'b']
    print(a)
    print(type(filter(None, a)))
    print(filter(None, a))


if __name__ == '__main__':
    main()
