# coding: utf-8
from subprocess import call


def main():
    retcode1 = call(["ls", "./"])
    print('retcode1: {}'.format(retcode1))
    retcode2 = call(["ls", "./not/existed/path"])
    print('retcode2: {}'.format(retcode2))


if __name__ == '__main__':
    main()
