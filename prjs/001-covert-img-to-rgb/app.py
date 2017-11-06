# coding: utf-8
from PIL import Image, ImageCms


def covert_a():
    img = Image.open('./img/in.jpg')
    img = img.convert('RGB')
    img.save('./img/out_a.jpg')


def covert_b():
    img = Image.open("./img/in.jpg")
    img = ImageCms.profileToProfile(img, './icc/JapanColor2001Coated.icc', './icc/sRGB Color Space Profile.icm',
                                    renderingIntent=0, outputMode='RGB')
    img.save('./img/out_b.jpg', quality=100)


def main():
    covert_a()
    covert_b()


if __name__ == '__main__':
    main()
