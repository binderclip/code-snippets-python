# coding: utf-8
from config import Config


def read_it():
    print('read Config.FOO: {}'.format(Config.FOO))


def main():
    read_it()


if __name__ == '__main__':
    main()
