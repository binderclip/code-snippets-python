# coding: utf-8
from subprocess import run


def main():
    run(["pwd"])
    run(["echo", "hello", "world"])
    run(["sleep", "1"])
    print(1)
    run(["sleep", "1"])
    print(2)
    run(["sleep", "1"])
    print(3)


if __name__ == '__main__':
    main()
