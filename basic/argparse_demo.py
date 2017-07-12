# coding: utf-8
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", help='debug mode on')

    args = parser.parse_args()

    print args
    print args.debug


if __name__ == '__main__':
    main()
