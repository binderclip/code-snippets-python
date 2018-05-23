from typing import List
from pydantic import BaseModel


class Foo(BaseModel):
    foo_a: int
    foo_b: int


class Bar(BaseModel):
    foo: Foo
    bar_a: int


def compare_two_model_obj(obj_a, obj_b):
    return obj_a.dict() == obj_b.dict()


def main():
    a = Bar(**{
        'foo': {
            'foo_a': 1,
            'foo_b': 2,
        },
        'bar_a': 3,
    })
    b = Bar(**{
        'foo': {
            'foo_a': 1,
            'foo_b': 2,
        },
        'bar_a': 3,
    })
    c = Bar(**{
        'foo': {
            'foo_a': 11,
            'foo_b': 2,
        },
        'bar_a': 3,
    })
    d = Bar(**{
        'foo': {
            'foo_a': 1,
            'foo_b': 2,
        },
        'bar_a': 31,
    })
    print('a == b ? {}'.format(compare_two_model_obj(a, b)))
    print('a == c ? {}'.format(compare_two_model_obj(a, c)))
    print('a == d ? {}'.format(compare_two_model_obj(a, d)))


if __name__ == '__main__':
    main()
