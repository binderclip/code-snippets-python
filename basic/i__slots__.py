import sys


class Image1(object):
    pass


class Image2(object):
    __slots__ = ['id', 'caption', 'url']


def set_obj(obj):
    obj.id = 1
    obj.caption = 'capppppppppp'
    obj.url = 'uuuuuuuuuuuuuuu'


def main():
    img1 = Image1()
    img2 = Image2()

    print(sys.getsizeof(img1))
    print(sys.getsizeof(img2))

    set_obj(img1)
    set_obj(img2)

    print(img1.__dict__)
    # print(img2.__dict__) AttributeError: 'Image2' object has no attribute '__dict__'

    print(sys.getsizeof(img1))
    print(sys.getsizeof(img2))


if __name__ == '__main__':
    main()
