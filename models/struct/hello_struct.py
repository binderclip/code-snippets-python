# coding: utf-8
from struct import pack, unpack
from base64 import urlsafe_b64encode, urlsafe_b64decode


def main():
    print urlsafe_b64encode(pack('L', 123))
    print urlsafe_b64encode(pack('L', 1234567))
    print urlsafe_b64encode(pack('L', 1234567890))
    print urlsafe_b64encode(pack('L', 1234567890123))
    print urlsafe_b64encode(pack('L', 12345678901234567))
    print urlsafe_b64encode(pack('L', 130000000000000000))
    print urlsafe_b64encode(pack('L', 990000000000000000))
    print unpack('L', urlsafe_b64decode('AADNrE_azQE='))[0]
    print unpack('L', urlsafe_b64decode('AACjN8EvvQ0='))[0]


if __name__ == '__main__':
    main()
