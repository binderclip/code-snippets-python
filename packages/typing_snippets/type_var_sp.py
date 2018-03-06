# coding: utf-8
from typing import TypeVar, Sequence


T = TypeVar('T')
A = TypeVar('A', str, bytes)


def repeat(x: T, n: int) -> Sequence[T]:
    """Return a list containing n references to x."""
    return [x]*n


def longest(x: A, y: A) -> A:
    """Return the longest of two strings."""
    print(len(x), len(y))
    return x if len(x) >= len(y) else y


def main():
    print(repeat('ha', 20))
    print(longest('big watermelon', '大西瓜🍉'))
    print(longest('big watermelon'.encode('utf-8'), '大西瓜🍉'.encode('utf-8')))

if __name__ == '__main__':
    main()
