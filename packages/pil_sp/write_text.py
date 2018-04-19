from PIL import Image, ImageFont, ImageDraw


def main():
    im = Image.new("RGB", (600, 600), "#000")
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("SourceHanSansCN-Normal.otf", 33)
    draw.text((10, 25), "大西瓜", font=font, fill="#F78")
    im.show()


if __name__ == '__main__':
    main()
