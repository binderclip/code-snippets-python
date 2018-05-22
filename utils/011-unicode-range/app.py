def is_chinese_char(c):
    """判断一个 unicode 字符是否是汉字"""
    return '\u4e00' <= c <= '\u9fa5'


def is_number_char(c):
    """判断一个 unicode 字符是否是数字"""
    return '\u0030' <= c <= '\u0039'


def is_alphabet_char(c):
    """判断一个 unicode 字符是否是英文字母"""
    return '\u0041' <= c <= '\u005a' or '\u0061' <= c <= '\u007a'


def main():
    c = '中'
    print('{} {}'.format(c, is_chinese_char(c)))
    c = '國'
    print('{} {}'.format(c, is_chinese_char(c)))
    c = '國'
    print('{} {}'.format(c, is_chinese_char(c)))
    c = '冇'
    print('{} {}'.format(c, is_chinese_char(c)))
    c = 'の'
    print('{} {}'.format(c, is_chinese_char(c)))
    c = 'な'
    print('{} {}'.format(c, is_chinese_char(c)))
    c = '漢'
    print('{} {}'.format(c, is_chinese_char(c)))
    c = '말'
    print('{} {}'.format(c, is_chinese_char(c)))
    c = '@'
    print('{} {}'.format(c, is_alphabet_char(c)))
    c = '0'
    print('{} {}'.format(c, is_number_char(c)))


if __name__ == '__main__':
    main()
