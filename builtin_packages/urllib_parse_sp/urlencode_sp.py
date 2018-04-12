from urllib.parse import urlencode


def main():
    params = {'lang': 'en', 'tag': 'python'}
    print(urlencode(params))

    params = {'foo': 'Az0 +-_./\\'}
    print(urlencode(params))


if __name__ == '__main__':
    main()
