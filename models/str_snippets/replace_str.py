# coding: utf-8


def replace_str():
    print('===== replace_str =====')
    s1 = u"aba"
    print('{} -> {}'.format(s1, s1.replace('a', 'A')))


def replace_str_code_test():
    print('===== replace_str_code_test =====')
    s1 = u"－－－"
    s2 = "－－－"
    print(u'{} -> {}'.format(s1, s1.replace(u'－', u'-')))
    print(u'{} -> {}'.format(s1, s1.replace(u'－', '-')))
    # print(u'{} -> {}'.format(s1, s1.replace('－', u'-')))    # UnicodeDecodeError
    # print(u'{} -> {}'.format(s1, s1.replace('－', '-')))    # UnicodeDecodeError
    print('{} -> {}'.format(s2, s2.replace('－', '-')))
    # print('{} -> {}'.format(s2, s2.replace(u'－', u'-')))    # UnicodeDecodeError
    # print('{} -> {}'.format(s2, s2.replace('－', u'-')))     # UnicodeDecodeError
    # print('{} -> {}'.format(s2, s2.replace(u'－', '-')))     # UnicodeDecodeError


def main():
    replace_str()
    replace_str_code_test()


if __name__ == '__main__':
    main()
