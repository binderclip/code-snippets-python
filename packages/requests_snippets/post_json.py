import requests


def main():
    url = 'https://httpbin.org/post'
    data = {
        'foo': 'bar',
    }
    print(requests.post(url, json=data).json())
    print(requests.post(url, data=data).json())


if __name__ == '__main__':
    main()
