from urllib.parse import parse_qsl


def main():
    qs = 'lang=en&tag=python&tag=python3'
    print(parse_qsl(qs))


if __name__ == '__main__':
    main()
