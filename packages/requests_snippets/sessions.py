import requests


def main():
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
    r = s.get("http://httpbin.org/cookies")
    print(r.text)
    r = requests.get("http://httpbin.org/cookies")
    print(r.text)


if __name__ == '__main__':
    main()

# http://docs.python-requests.org/en/latest/user/advanced/
