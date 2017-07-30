# coding: utf-8
from config import Config
from read_config import read_it


def set_it():
    Config.FOO = 'baz'


def main():
    read_it()
    set_it()
    read_it()


if __name__ == '__main__':
    main()
