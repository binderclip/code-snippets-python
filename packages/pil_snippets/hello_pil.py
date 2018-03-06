# coding: utf-8
from __future__ import print_function
from PIL import Image


def main():
    im = Image.open("../common_img/in.jpg")
    print(im.format, im.size, im.mode)


if __name__ == '__main__':
    main()
