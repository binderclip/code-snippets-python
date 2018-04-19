import imghdr
import io
import shutil

import requests


def main():
    image_url = 'https://qn.cdn.cliiip.com/imgs/u/c2eddd32-754b-4e3b-975b-86741561bda5.png'
    r = requests.get(image_url, stream=True)
    with io.BytesIO() as f:
        r.raw.decode_content = True     # ?
        shutil.copyfileobj(r.raw, f)
        f.seek(0)

        r = requests.post(
            'https://httpbin.org/post',
            files={
                'media': f
            }
        )
        print(r.json())

        f.name = 'imagefile'
        f.seek(0)
        r = requests.post(
            'https://httpbin.org/post',
            files={
                'media': (f.name, f),
            }
        )
        print(r.json())


if __name__ == '__main__':
    main()
