import base64


# urlsafe_b64encode doc: The alphabet uses '-' instead of '+' and '_' instead of '/'.


def urlsafe_encode_and_decode(s):
    print('=== urlsafe_encode_and_decode ===')
    print(s)
    s_encoded = base64.urlsafe_b64encode(s.encode('utf-8'))
    print(s_encoded)
    print(base64.urlsafe_b64decode(s_encoded).decode('utf-8'))


def main():
    urlsafe_encode_and_decode('hello')


if __name__ == '__main__':
    main()
