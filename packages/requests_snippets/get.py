import requests


def main():
    r = requests.get('http://httpbin.org/get', params={'foo': 'bar'})
    print(r.json())


if __name__ == '__main__':
    main()
