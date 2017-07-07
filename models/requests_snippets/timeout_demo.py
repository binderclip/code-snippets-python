# coding: utf-8
import requests
from requests.exceptions import Timeout


def main():
    try:
        r = requests.get('http://httpbin.org/delay/3', timeout=(3, 3))
        print(r.status_code)
    except Timeout:
        print("timeout")


if __name__ == '__main__':
    main()
