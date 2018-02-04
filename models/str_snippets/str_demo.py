# coding: utf-8


def split_str():
    print("===== split_str =====")
    url = 'www.google.com.hk'
    print(url.split('.'))


def split_unicode():
    print("===== split_unicode =====")
    text = u'正义、秩序、自由'
    print(text.split(u'、'))
    template = u'城市-职业-昵称'
    print(template.split('-'))


def sort_str():
    print("===== sort_str =====")
    str_list = [
        "0802aaa",
        "1202aa",
        "0209aaa",
        "0812ccc",
        "0802ddd",
    ]
    str_list.sort()
    print(str_list)


def get_char_of_str():
    print("===== get_char_of_str =====")
    s = 'hello'
    for c in s:
        print(c)


def main():
    split_str()
    split_unicode()
    sort_str()
    get_char_of_str()


if __name__ == '__main__':
    main()
