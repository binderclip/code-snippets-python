from pydantic import BaseModel


class Foo(BaseModel):
    bar: str = None
    baz: int = 10


def main():
    foo = Foo.parse_obj({})
    print(foo)


if __name__ == '__main__':
    main()
