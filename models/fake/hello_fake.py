# coding: utf-8
from faker import Factory


def main():
    fake = Factory.create()
    print("Hello, {}!".format(fake.name()))


if __name__ == '__main__':
    main()
