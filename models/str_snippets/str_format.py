# coding: utf-8


def format_number():
    print("=== format_number ===")
    print('{:0>2d}:{:0>2d}'.format(3, 3))
    print('{:0>2d}:{:0>2d}'.format(23, 3))
    print('{:0>2d}:{:0>2d}'.format(123, 3))


def main():
    format_number()


if __name__ == '__main__':
    main()

# ref: http://www.runoob.com/python/att-string-format.html
