# coding: utf-8
import shutil
import requests


def save_img(path, url):
    print(path)

    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, 'wb') as f:
            r.raw.decode_content = True     # ?
            shutil.copyfileobj(r.raw, f)


def main():
    img_path = "xxx.jpg"
    url = "http://s2.cdn.xiachufang.com/fe11b65e673511e7947d0242ac110002_850w_567h.jpg"
    save_img(img_path, url)


if __name__ == '__main__':
    main()


# stream=True: Advanced Usage — Requests 2.18.1 documentation http://docs.python-requests.org/en/master/user/advanced/#body-content-workflow
