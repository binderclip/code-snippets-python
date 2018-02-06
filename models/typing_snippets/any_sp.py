# coding: utf-8
from typing import Any


def foo(item: Any) -> Any:
    return item


def bar(s: str) -> None:
    print(s)


def main():
    bar(foo('hello'))
    bar(foo(12))


if __name__ == '__main__':
    main()
