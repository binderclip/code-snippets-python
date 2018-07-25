import base64
import hashlib


def hash_string_to_int1(my_str):
    return int(hashlib.sha256(my_str.encode('utf-8')).hexdigest(), 16)


def hash_string_to_int2(my_str: str):
    return int(hashlib.md5(my_str.encode('utf-8')).hexdigest(), 16)


def hash_string(my_str: str):
    return hashlib.md5(my_str.encode('utf-8')).hexdigest()


def print_digest1(my_str):
    m = hashlib.sha224()
    m.update(my_str.encode('utf-8'))
    print(m.digest())
    print(m.digest_size)
    print(m.block_size)


def print_digest2(my_str):
    m = hashlib.sha1()
    m.update(my_str.encode('utf-8'))
    print(m.digest())
    print(m.digest_size)
    print(m.block_size)


def print_hash_data():
    print('=== print_hash_data ===')
    print(hashlib.algorithms_available)
    print(hashlib.algorithms_guaranteed)
    m = hashlib.md5()
    print(m.name)


def main():
    print(hash_string_to_int1('hello world'))
    print(hash_string_to_int1('hello world!'))
    print(hash_string_to_int2('hello world'))
    print(hash_string_to_int2('hello world!'))
    print(hash_string('hello world'))
    print(hash_string('hello world!'))
    print_digest1('hello')
    print_digest2('hello')
    print_hash_data()


if __name__ == '__main__':
    main()
