# coding: utf-8
from typing import Callable, List


def feeder(get_next_item: Callable[[], str]) -> None:
    pass


def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None]) -> None:
    pass


def main():
    print('Hello')


if __name__ == '__main__':
    main()
