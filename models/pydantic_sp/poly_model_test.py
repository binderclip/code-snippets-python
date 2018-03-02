from enum import IntEnum

from pydantic import BaseModel, validator


class FooTypeEnum(IntEnum):
    A = 1
    B = 2


class Foo(BaseModel):
    type: int

    def __init__(self, **data):
        print('>>> __init__')
        print(data)
        super(Foo, self).__init__(**data)

    @classmethod
    def validate(cls, value):
        print('>>> validate')
        print(value)
        type_to_model = {
            FooTypeEnum.A: FooA,
            FooTypeEnum.B: FooB,
        }
        try:
            return type_to_model[value['type']](**value)
        except KeyError:
            raise ValueError('xxx')


class FooA(Foo):
    a: str


class FooB(Foo):
    b: str


class Bar(BaseModel):
    foo: Foo = ...

    @validator('foo')
    def test_vali(cls, v):
        print('>>> test vali')
        print(cls)
        print(v)
        return v


m = Bar(foo={'type': FooTypeEnum.A, 'a': 'aaa'})
print(m)
# > Bar foo=<FooA type=1 a='aaa'>
print(m.dict())
# > {'foo': {'type': 1, 'a': 'aaa'}}
m = Bar(foo={'type': FooTypeEnum.B, 'b': 'bbb'})
print(m)
# > Bar foo=<FooB type=2 b='bbb'>
print(m.dict())
# > {'foo': {'type': 2, 'b': 'bbb'}}
