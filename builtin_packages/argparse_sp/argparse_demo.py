# coding: utf-8
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", help='debug mode on')
    parser.add_argument("your_name", help="your name")

    args = parser.parse_args()

    print(args)
    print(args.debug)
    print(args.your_name)


if __name__ == '__main__':
    main()
