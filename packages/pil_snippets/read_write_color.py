# coding: utf-8
from __future__ import print_function
from PIL import Image, ImageDraw


def print_all_pixel_data(im):
    w, h = im.size
    for i in range(h):
        s = ','.join(map(str, [im.getpixel((j, i)) for j in range(w / 100)]))
        print(s)


def draw_points(im):
    x, y = 10, 20
    im.putpixel((x, y), (255, 255, 255))
    im.putpixel((x, y - 1), (255, 0, 0))
    im.putpixel((x + 1, y), (0, 255, 0))
    im.putpixel((x, y + 1), (0, 0, 255))
    im.putpixel((x - 1, y), (0, 255, 0))


def draw_lines(im):
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=128)
    draw.line((0, im.size[1], im.size[0], 0), fill=128, width=3)
    del draw


def main():
    im = Image.open("../common_img/jump_jump.jpg")
    # print_all_pixel_data(im)
    # draw_points(im)
    draw_lines(im)
    im.save("../common_img/jump_jump2.jpg")


if __name__ == '__main__':
    main()
