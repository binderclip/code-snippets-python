from enum import IntEnum

from pydantic import BaseModel


class FooTypeEnum(IntEnum):
    A = 1
    B = 2


class Foo(BaseModel):
    type: int

    @classmethod
    def validate(cls, value):
        type_to_model = {
            FooTypeEnum.A: FooA,
            FooTypeEnum.B: FooB,
            None: cls
        }
        _type = value.get('type', None)
        try:
            return type_to_model[_type](**value)
        except KeyError:
            raise TypeError(f'no model for type: {_type}')


class FooA(Foo):
    a: str


class FooB(Foo):
    b: str


class Bar(BaseModel):
    foo: Foo = ...


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
