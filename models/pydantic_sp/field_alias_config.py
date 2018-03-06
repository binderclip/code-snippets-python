from pydantic import BaseModel


class Foo(BaseModel):
    bar: str
    baz: str

    class Config:
        fields = {
            'bar': {
                'alias': 'Bar',
            },
        }


def main():
    foo_data = {
        "Bar": "barrrrr",
        "baz": "bazzzzz",
    }
    foo = Foo.parse_obj(foo_data)
    print(foo)
    print(foo.dict())


if __name__ == '__main__':
    main()
