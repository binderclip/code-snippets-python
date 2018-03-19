def main():
    i = 105555555
    s = str(i)
    print(s)
    print(int(s))

    hex_str1 = hex(i)
    print(hex_str1)
    print(type(hex_str1))
    print(int(hex_str1, 16))

    hex_str2 = '{:x}'.format(i)
    print(hex_str2)
    print(int(hex_str2, 16))

    print('{:04x}'.format(1))
    print('{:04x}'.format(100000))


if __name__ == '__main__':
    main()
