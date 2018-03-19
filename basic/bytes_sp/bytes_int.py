def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def int_from_bytes(xbytes):
    return int.from_bytes(xbytes, 'big')


def main():
    print(bytes([255]))
    # print(bytes([1024]))    # ValueError: bytes must be in range(0, 256)

    b = int_to_bytes(1024)
    print(b)
    i = int_from_bytes(b)
    print(i)


if __name__ == '__main__':
    main()



# https://stackoverflow.com/a/30375198/3936457
