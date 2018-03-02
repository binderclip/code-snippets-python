from typing import List, Union
from enum import IntEnum

from pydantic import BaseModel


class FooTypeEnum(IntEnum):
    A = 1
    B = 2


class Foo(BaseModel):
    type: FooTypeEnum


class FooA(Foo):
    a: str


class FooB(Foo):
    b: str


class Bar(BaseModel):
    foo: Union[FooA, FooB]


class Baz(BaseModel):
    foos: List[Union[FooA, FooB]]


m = Bar(foo={'type': FooTypeEnum.A, 'a': 'aaa'})
print(m)
# Bar foo=<FooA type=1 a='aaa'>
print(m.dict())
# {'foo': {'type': 1, 'a': 'aaa'}}
m = Bar(foo={'type': FooTypeEnum.B, 'b': 'bbb'})
print(m)
# Bar foo=<FooB type=2 b='bbb'>
print(m.dict())
# {'foo': {'type': 2, 'b': 'bbb'}}

# m = Bar(foo={'type': FooTypeEnum.B, 'c': 'bbb'})
# error ...
# m = Bar(foo={'type': 3, 'c': 'bbb'})
# error ...
# m = Bar(foo={'c': 'bbb'})
# error ...


m = Baz(foos=[
    {'type': FooTypeEnum.A, 'a': 'aaa'},
    {'type': FooTypeEnum.B, 'b': 'bbb'},
])
print(m)
print(m.dict())

# https://github.com/samuelcolvin/pydantic/issues/135
