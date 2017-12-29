# coding: utf-8
from __future__ import print_function
from PIL import Image


def main():
    im = Image.open("../common_img/jump_jump.jpg")
    print(im.format, im.size, im.mode)
    w, h = im.size
    for i in range(h):
        s = ','.join(map(str, [im.getpixel((j, i)) for j in range(w / 100)]))
        print(s)


if __name__ == '__main__':
    main()
