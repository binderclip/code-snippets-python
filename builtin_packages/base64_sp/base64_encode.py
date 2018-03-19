import base64


def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def print_b64encode(bs):
    print(base64.b64encode(bs))


def main():
    print_b64encode(b'\xff\xff\xff')
    print_b64encode('a'.encode('utf-8'))
    print_b64encode('aa'.encode('utf-8'))
    print_b64encode('aaa'.encode('utf-8'))
    print_b64encode('aaaa'.encode('utf-8'))
    print_b64encode(int_to_bytes(105697106))


if __name__ == '__main__':
    main()
