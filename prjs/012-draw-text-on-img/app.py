from PIL import Image, ImageFont, ImageDraw

data = [
    {
        'id': '3c1d4d3c-c3b4-4b81-804a-0f82b6f35e29',
        'name': '坂田银八',
    },
    {
        'id': 'b46c36c6-9d84-49a6-a706-a8e216431184',
        'name': '志村新八',
    }
]


def main(bg_img_file_name, configs):
    for user in configs:
        draw_text_on_image(bg_img_file_name, user)


def draw_text_on_image(bg_img_file_name, user):
    im = Image.open(bg_img_file_name)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("SourceHanSansCN-Regular.otf", 33)
    draw.text((190, 560), f"{user['name']}同学：", font=font, fill="#000")
    im.save(f"out/{user['id']}.png")


def _create_bg_image():
    im = Image.new("RGB", (750, 1132), "#FFF")
    im.save('bg.png')


if __name__ == '__main__':
    main(
        bg_img_file_name='bg.png',
        configs=data,
    )

