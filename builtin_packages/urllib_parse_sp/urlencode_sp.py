from urllib.parse import urlencode, unquote, quote


def main():
    params = {'lang': 'en', 'tag': 'python'}
    print(urlencode(params))

    params = {'foo': 'Az0 +-_./\\'}
    print(urlencode(params))

    params = {'bwm': '大西瓜'}
    print(urlencode(params))

    print(quote('大西瓜'))
    print(unquote(quote('大西瓜')))


if __name__ == '__main__':
    main()
