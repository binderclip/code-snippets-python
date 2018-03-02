from dataclasses import dataclass, fields, field


@dataclass
class C(object):
    # basic
    field_a: str


@dataclass
class C1(object):
    # with default
    field_a: str = field(default='')


@dataclass
class C2(object):
    field_a: str
    field_b: int

    @classmethod
    def get_fields(cls):
        return fields(cls)


class Foo(object):
    def __init__(self, foo):
        self.foo = foo


def main():
    # get all fields
    print(fields(C))
    print(C2.get_fields())
    print(C2.__dict__)


if __name__ == '__main__':
    main()
