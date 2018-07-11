import requests


def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iOS 11.4 like Mac OS X)",
    }
    r = requests.get('https://httpbin.org/headers', headers=headers)
    print(r.json())


if __name__ == '__main__':
    main()
