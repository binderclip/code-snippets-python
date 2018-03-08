import requests


def main():
    proxies = {'http': 'http://localhost:8886', 'https': 'http://localhost:8886'}
    r = requests.get('https://httpbin.org/get', proxies=proxies, verify=False)
    print(r.json())


if __name__ == '__main__':
    main()


# http://www.cnblogs.com/clip/p/python-requests-proxy-and-ssl-config.html
# https://stackoverflow.com/questions/10667960/python-requests-throwing-sslerror
