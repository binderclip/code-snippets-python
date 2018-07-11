import requests


def main():

    url = 'https://httpbin.org/post'
    with open('../_common_img/xxx.png', 'rb') as f:
        r = requests.post(url, files={'image': ('xxx.png', f, 'image/png')})
        print(r.json())


if __name__ == '__main__':
    main()
