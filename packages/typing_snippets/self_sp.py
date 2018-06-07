from typing import TypeVar, Type

T = TypeVar('T', bound='C')
class C:
    def __init__(self, a: str, b: int):
        self.a = a
        self.b = b

    @classmethod
    def factory(cls: Type[T]) -> T:
        return C('hello', 123)


c = C.factory()
print(c.a, c.b)


# https://github.com/python/mypy/issues/1212
