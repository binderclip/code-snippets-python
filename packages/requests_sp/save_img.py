# coding: utf-8
import shutil
import requests


def save_img(path, url):
    print(path)

    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(path, 'wb') as f:
            r.raw.decode_content = True     #      # decode based on content-encoding
            print(type(r.raw))
            shutil.copyfileobj(r.raw, f)


def main():
    img_path = "xxx.jpg"
    url = "https://qn.cdn.cliiip.com/imgs/u/4c3f70fd-f1c4-4232-a6ff-9228ce164fc5.png"
    save_img(img_path, url)


if __name__ == '__main__':
    main()


# stream=True: Advanced Usage — Requests 2.18.1 documentation http://docs.python-requests.org/en/master/user/advanced/#body-content-workflow
