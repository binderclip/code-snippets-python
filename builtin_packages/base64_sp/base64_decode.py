import base64


def print_b64decode(bs):
    print(base64.b64decode(bs))


def main():
    print_b64decode(b'////')
    print_b64decode(b'YQ==')
    print_b64decode(b'YWE=')
    print_b64decode(b'YWFh')
    print_b64decode(b'YWFhYQ==')
    print_b64decode(b'BkzPUg==')


if __name__ == '__main__':
    main()
