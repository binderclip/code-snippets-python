# coding: utf-8


def str_isdigit():
    print("=== str_isdigit ===")
    print('"123".isdigit(): {}'.format('123'.isdigit()))
    print('"0x1234".isdigit(): {}'.format('0x1234'.isdigit()))
    print('"0123".isdigit(): {}'.format('0123'.isdigit()))
    print('"xc123".isdigit(): {}'.format('xc123'.isdigit()))


def main():
    str_isdigit()


if __name__ == '__main__':
    main()
