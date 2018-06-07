# coding: utf-8
from typing import Union, Optional


def foo(x: Union[str, int]) -> None:
    print(x)


def foo2(x: int) -> Union[str, None]:
    if x < 0:
        return
    return str(x)


def foo3(x: int) -> Optional[str]:
    return foo2(x)


def main():
    foo(1)
    foo('a')
    # foo([1, 2])

    foo2(10)
    foo2(-10)
    foo3(10)
    foo3(-10)


if __name__ == '__main__':
    main()
