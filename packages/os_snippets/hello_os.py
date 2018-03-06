# coding: utf-8
import os
import os
import platform


def main():
    print(os.name)
    print(platform.system())
    print(platform.release())


if __name__ == '__main__':
    main()
