# coding: utf-8
from typing import Union


def foo(x: Union[str, int]) -> None:
    print(x)


def main():
    foo(1)
    foo('a')
    # foo([1, 2])


if __name__ == '__main__':
    main()
