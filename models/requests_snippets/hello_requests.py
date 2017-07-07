# coding: utf-8
import requests

def main():
    r = requests.get('http://httpbin.org/get')
    print(r.status_code)
    print(r.headers)
    print(r.text)


if __name__ == '__main__':
    main()
