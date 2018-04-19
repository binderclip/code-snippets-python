from PIL import Image


def main():
    im = Image.new("RGB", (200, 200), "#FFF")
    im.show()


if __name__ == '__main__':
    main()
