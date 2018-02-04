# coding: utf-8
import os


def main():
    print(os.environ["HOME"])
    print(os.environ['PATH'])
    print(os.environ.get('NOT_EXIST'))

    os.environ['FOO'] = 'BAR'
    print(os.environ['FOO'])


if __name__ == '__main__':
    main()
