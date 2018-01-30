# coding: utf-8


def greeting(name: str) -> str:
    if not name:
        return 123      # PyCharm 会有提示，但是运行不会有异常
    return 'Hello ' + name


def main():
    print(greeting("clip"))
    # print(greeting(123))    # TypeError: must be str, not int
    print(greeting(""))

if __name__ == '__main__':
    main()


# [26.1. typing — Support for type hints — Python 3.6.4 documentation](https://docs.python.org/3/library/typing.html#module-typing)
