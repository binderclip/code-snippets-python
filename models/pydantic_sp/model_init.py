from pydantic import BaseModel


class Foo(BaseModel):
    bar: int = 0
    baz: str = ''


def main():
    # use default
    foo = Foo()
    print(foo)
    # set values
    foo.bar = 3
    foo.baz = 'x'
    print(foo)
    # init with kwargs
    foo = Foo(bar=1, baz='2')
    print(foo)
    # init with a dict
    foo = Foo.parse_obj({"bar": 1, "baz": '2'})
    print(foo)


if __name__ == '__main__':
    main()
