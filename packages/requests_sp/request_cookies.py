import requests


def main():
    cookies = {
        "t": "ttt",
    }
    r = requests.get('https://httpbin.org/cookies', cookies=cookies)
    print(r.json())


if __name__ == '__main__':
    main()
