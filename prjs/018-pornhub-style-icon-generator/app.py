from PIL import Image, ImageFont, ImageDraw


def rounded_rectangle(self: ImageDraw, p1p2, corner_radius, fill=None, outline=None):
    x1, y1, x2, y2 = p1p2
    self.rectangle(
        [
            (x1, y1 + corner_radius),
            (x2, y2 - corner_radius)
        ],
        fill=fill,
        outline=outline
    )
    self.rectangle(
        [
            (x1 + corner_radius, y1),
            (x2 - corner_radius, y2)
        ],
        fill=fill,
        outline=outline
    )
    self.pieslice([(x1, y1), (x1 + corner_radius * 2, y1 + corner_radius * 2)],
        180,
        270,
        fill=fill,
        outline=outline
    )
    self.pieslice([(x2 - corner_radius * 2, y2 - corner_radius * 2), (x2, y2)],
        0,
        90,
        fill=fill,
        outline=outline
    )
    self.pieslice([(x1, y2 - corner_radius * 2), (x1 + corner_radius * 2, y2)],
        90,
        180,
        fill=fill,
        outline=outline
    )
    self.pieslice([(x2 - corner_radius * 2, y1), (x2, y1 + corner_radius * 2)],
        270,
        360,
        fill=fill,
        outline=outline
    )


ImageDraw.ImageDraw.rounded_rectangle = rounded_rectangle


def main():
    text = "hub"

    font_size = 200
    font = ImageFont.truetype("Arial Bold.ttf", font_size)
    w, h = font.getsize(text)

    y_offset = int(font_size / 11)
    x_margin = int(font_size / 20)  # 文字对矩形的 margin
    y_margin = int(font_size / 10)
    r_margin = int(font_size / 10) # 整个矩形的 margin

    im = Image.new("RGB", (w + (x_margin + r_margin) * 2, h + (y_margin + r_margin) * 2), "#000")
    draw = ImageDraw.Draw(im)

    x_r, y_r = r_margin, r_margin
    x_t, y_t = r_margin + x_margin, r_margin + y_margin - y_offset

    draw.rounded_rectangle((x_r, y_r, x_r + w + x_margin * 2, y_r + h + y_margin * 2), w / 20, fill='#F90')
    draw.text((x_t, y_t), text, font=font, fill="#000")
    im.save(f"hello.png")


if __name__ == '__main__':
    main()


# 这个用前端的方式生成更方便一些，就不继续往下实现了

# https://stackoverflow.com/questions/18869365/a-watermark-inside-a-rectangle-which-filled-the-certain-color
# https://stackoverflow.com/questions/7787375/python-imaging-library-pil-drawing-rounded-rectangle-with-gradient/50145023#50145023
