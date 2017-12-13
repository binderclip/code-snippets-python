# coding: utf-8


def format_number():
    print("=== format_number ===")
    print('{:0>2d}:{:0>2d}'.format(3, 3))
    print('{:0>2d}:{:0>2d}'.format(23, 3))
    print('{:0>2d}:{:0>2d}'.format(123, 3))
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


def main():
    format_number()


if __name__ == '__main__':
    main()

# ref: http://www.runoob.com/python/att-string-format.html
