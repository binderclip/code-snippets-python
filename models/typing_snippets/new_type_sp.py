# coding: utf-8
from typing import NewType

UserId = NewType('UserId', int)


def get_user_name(user_id: UserId) -> str:
    return {
        1: "foo",
        2: "bar"
    }.get(user_id)


def main():
    some_id = UserId(1)
    print(some_id)
    print(get_user_name(some_id))
    print(get_user_name(1))


if __name__ == '__main__':
    main()
