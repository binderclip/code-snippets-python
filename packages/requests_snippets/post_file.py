import requests


def main():
    url = 'https://httpbin.org/post'
    with open('xxx.jpg', 'rb') as f:
        r = requests.post(url, files=[('image', f)])
        print(r.json())


if __name__ == '__main__':
    main()
