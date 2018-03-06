# coding: utf-8
from base64 import urlsafe_b64encode, urlsafe_b64decode


def main():
    print(urlsafe_b64encode('abc/=%?&'))
    print(urlsafe_b64encode('100'))
    print(urlsafe_b64decode('MTAw'))


if __name__ == '__main__':
    main()
