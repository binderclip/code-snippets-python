def to_utf8(s):
    if isinstance(s, str):
        return s.encode('utf-8')
    return s


def to_unicode(s):
    if isinstance(s, bytes):
        return s.decode('utf-8')
    return s


def main():
    print(to_utf8('哈哈哈'), to_unicode(b'\xe5\x93\x88\xe5\x93\x88\xe5\x93\x88'))

    # print('哈哈哈'.encode('ascii'))  # UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-2: ordinal not in range(128)


if __name__ == '__main__':
    main()
