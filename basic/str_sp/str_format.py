# coding: utf-8


def format_number():
    print("=== format_number ===")
    print('{:>2d}:{:>2d}'.format(3, 3))
    print('{:>2d}:{:>2d}'.format(23, 3))
    print('{:>2d}:{:>2d}'.format(123, 3))
    print('-')
    print('{:0>2d}:{:0>2d}'.format(3, 3))
    print('{:0>2d}:{:0>2d}'.format(23, 3))
    print('{:0>2d}:{:0>2d}'.format(123, 3))
    print('-')
    print('{:0<2d}:{:0<2d}'.format(3, 3))
    print('{:0<2d}:{:0<2d}'.format(23, 3))
    print('{:0<2d}:{:0<2d}'.format(123, 3))
    print('-')
    print('{:02d}:{:02d}'.format(3, 3))
    print('{:02d}:{:02d}'.format(23, 3))
    print('{:02d}:{:02d}'.format(123, 3))
    print('-')
    print('{:0<2d}:{:0<2d}'.format(3, 3))
    print('{:0<2d}:{:0<2d}'.format(23, 3))
    print('{:0<2d}:{:0<2d}'.format(123, 3))

    print('-')
    print('{:.2f}'.format(123.45678))   # 会自动四舍五入
    print('{:.2%}'.format(0.12345))     # 用百分号的形式
    print('-')
    print("{0:b}".format(0x1234))       # 最前面的 0 是参数的标号
    print("{0:16b}".format(0x1234))
    print("{0:016b}".format(0x1234))

    print('-')
    print("{:x}".format(2 ** 4 - 1))
    print("{:x}".format(2 ** 8 - 10))
    print("{:x}".format(2 ** 16 - 1))
    print('-')
    print("{:06x}".format(2 ** 4 - 1))
    print("{:06x}".format(2 ** 8 - 10))
    print("{:06x}".format(2 ** 16 - 1))



def main():
    format_number()


if __name__ == '__main__':
    main()

# http://www.runoob.com/python/att-string-format.html
# https://stackoverflow.com/a/18946037/3936457

