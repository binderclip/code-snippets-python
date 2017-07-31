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


def main():
    split_str()
    split_unicode()


if __name__ == '__main__':
    main()
