from pydantic import BaseModel, ValidationError, validator


class Foo(BaseModel):
    bar: int
    baz: str

    @validator('bar')
    def bar_less_than_10(cls, v):
        if v >= 10:
            raise ValueError('bar 必须大于 10')
        return v


def format_validation_error(e):
    error_strs = []
    for k, v in e.errors_dict.items():
        error_strs.append(f'{k}: {v["error_msg"]}')
    return '\n'.join(error_strs)


def main():
    # missing error
    try:
        foo = Foo()
    except ValidationError as e:
        print(e)
        print(e.json())
    # type error
    try:
        foo = Foo(bar='r', baz='z')
    except ValidationError as e:
        print(e)
        print(e.json())
    # custom validator error
    try:
        foo = Foo(bar=10, baz='z')
    except ValidationError as e:
        print(e)
        print(e.display_errors)
        print(e.json())
        # custom format
        print(format_validation_error(e))


if __name__ == '__main__':
    main()
