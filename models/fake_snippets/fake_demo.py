# coding: utf-8
from faker import Factory


def main():
    fake = Factory.create()
    print("name: {}".format(fake.name()))
    print("text: {}".format(fake.text()))


if __name__ == '__main__':
    main()
