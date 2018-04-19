from PIL import Image


def main():
    im = Image.open("../_common_img/in.jpg")
    print(im.format, im.size, im.mode)
    print(type(im.mode))
    im.show()


if __name__ == '__main__':
    main()
