# coding: utf-8
from typing import List


def greeting(name: str) -> str:
    if not name:
        return 123      # PyCharm 会有提示，但是运行不会有异常
    return 'Hello ' + name


def greeting_many(names: List[str]) -> List[str]:
    return [greeting(name) for name in names]


def main():
    print(greeting("clip"))
    # print(greeting(123))    # TypeError: must be str, not int
    print(greeting(""))
    print(greeting_many(['clip', 'cliip', 'cliiip']))


if __name__ == '__main__':
    main()
