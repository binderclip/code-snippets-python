from pypinyin import lazy_pinyin


def main():
    print(lazy_pinyin('中国'))
    print(''.join(lazy_pinyin('大西瓜')))


if __name__ == '__main__':
    main()
