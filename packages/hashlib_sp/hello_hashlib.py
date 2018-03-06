# coding: utf-8
import hashlib


def hash_string_to_int(my_str):
    return int(hashlib.sha256(my_str.encode('utf-8')).hexdigest(), 16)


def get_md5(my_str: str):
    m = hashlib.md5()
    m.update(my_str.encode('utf-8'))
    return m.hexdigest()


def main():
    print(hash_string_to_int('hello world'))
    print(hash_string_to_int('hello world!'))
    print(get_md5('hello world'))
    print(get_md5('hello world!'))


if __name__ == '__main__':
    main()
