import shutil
import requests
import io


def main():
    url_down = 'https://qn.cdn.cliiip.com/imgs/u/4c3f70fd-f1c4-4232-a6ff-9228ce164fc5.png'
    url_up = 'https://httpbin.org/post'

    r = requests.get(url_down, stream=True)
    if r.status_code == 200:
        with io.BytesIO() as f:
            r.raw.decode_content = True     # decode based on content-encoding
            print(type(r.raw))
            shutil.copyfileobj(r.raw, f)
            f.seek(0)
            r = requests.post(url_up, files=[('image', f)])
            print(r.json())


if __name__ == '__main__':
    main()
