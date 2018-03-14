from urllib.parse import parse_qs


def main():
    qs = 'lang=en&tag=python&tag=python3'
    print(parse_qs(qs))
    qs = ''
    print(parse_qs(qs))


if __name__ == '__main__':
    main()
