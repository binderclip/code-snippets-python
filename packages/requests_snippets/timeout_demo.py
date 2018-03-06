# coding: utf-8
import requests
from requests.exceptions import Timeout


def main():
    try:
        r = requests.get('http://httpbin.org/delay/1', timeout=(3, 5))  # ConnectTimeout = 3, ReadTimeout = 5
        # r = requests.get('http://httpbin.org/delay/1', timeout=5)       # ConnectTimeout = ReadTimeout = 5
        print(r.status_code)
        print int(r.elapsed.total_seconds() * 1000)     # ms
    except Timeout:
        # http://docs.python-requests.org/en/master/_modules/requests/exceptions/
        # ConnectTimeout(ConnectionError, Timeout)
        # ReadTimeout(Timeout)
        print("timeout")


if __name__ == '__main__':
    main()
