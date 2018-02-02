# coding: utf-8
import hashlib


def hash_string_to_int(my_str):
    return int(hashlib.sha256(my_str.encode('utf-8')).hexdigest(), 16)


def main():
    print(hash_string_to_int('hello world'))
    print(hash_string_to_int('hello world!'))


if __name__ == '__main__':
    main()
