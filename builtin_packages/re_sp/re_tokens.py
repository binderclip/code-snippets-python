# coding: utf-8
import re


def add_space_after_hash(s):
    m = re.search(r'#(\S+)', s)
    if m:
        return '# {}'.format(m.group(1))
    return s


def find_str(s):
    m = re.search(r'https?://www\.example\.com\?abc_d=(\d+)', s)
    if m:
        return 'find: {} ||| {}'.format(m.group(0), m.group(1))
    return


def main():
    print(add_space_after_hash('##'))
    print(add_space_after_hash('#1'))
    print(add_space_after_hash('# 2'))
    print(add_space_after_hash('#大西瓜'))
    print(add_space_after_hash('#大西瓜#大西瓜'))
    print(find_str('https://www.example.com?abc_d=123'))
    print(find_str('http://www.example.com?abc_d=12345'))
    print(find_str('https://www.example.com?abc_d=1234589sdf'))
    print(find_str('https://www.example.com?abc_d=12345)dsf'))


if __name__ == '__main__':
    main()
