# coding: utf-8
from subprocess import call


def main():
    call(["pwd"])
    call(["echo", "hello", "world"])
    call(["sleep", "1"])
    print(1)
    call(["sleep", "1"])
    print(2)
    call(["sleep", "1"])
    print(3)


if __name__ == '__main__':
    main()
