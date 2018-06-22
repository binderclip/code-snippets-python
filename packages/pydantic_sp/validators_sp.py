import base64
from pydantic import BaseModel, ValidationError, validator, constr


class UserModel(BaseModel):
    name: constr(min_length=4, max_length=16)
    password1: str
    password2: str

    @validator('name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v


class IntNextCursorDTO(BaseModel):
    cursor: int = None
    size: int = 10

    # 用 pre 来先检查
    @validator('cursor', pre=True)
    def trans_str_cursor_to_int(cls, v):
        n = base64.urlsafe_b64decode(str(v).encode('utf-8')).decode('utf-8')
        return int(n)


class Foo(BaseModel):
    n: int


class Bar(BaseModel):
    foo: Foo
    n: int
    m: int

    @validator('m')
    def m_less_than_n(cls, v, values, **kwargs):
        print(f'm {values}')
        if 'n' in values and v >= values['n']:
            raise ValueError('m greater than n')
        return v

    @validator('n')
    def n_same_with_n(cls, v, values, **kwargs):
        print(f'n {values}')
        if 'foo' in values and v != values["foo"].n:
            raise ValueError('foo.n != n')
        return v


def basic_validator():
    print('=== basic_validator ===')
    print(UserModel(name='samuel colvin', password1='zxcvbn', password2='zxcvbn'))
    # > UserModel name='Samuel Colvin' password1='zxcvbn' password2='zxcvbn'

    try:
        UserModel(name='sam', password1='zxcvbn', password2='zxcvbn2')
    except ValidationError as e:
        print(e)
    # 2 errors validating input
    # name:
    #   length less than minimum allowed: 4 (error_type=ValueError track=ConstrainedStrValue)
    # password2:
    #   passwords do not match (error_type=ValueError track=str)

    try:
        UserModel(name='samuel', password1='zxcvbn', password2='zxcvbn')
    except ValidationError as e:
        print(e)
    # error validating input
    # name:
    #   must contain a space (error_type=ValueError track=ConstrainedStrValue)


def validator_with_pre():
    print('=== validator_with_pre ===')
    next_cursor = IntNextCursorDTO(cursor='Mg==', size='10')
    print(next_cursor)


def validator_with_multi_fields():
    print('=== validator_with_multi_fields ===')
    print(Bar(n=10, m=5, foo=Foo(n=10)))
    try:
        print(Bar(n=10, m=15, foo=Foo(n=10)))
    except ValidationError as e:
        print(e)
    try:
        print(Bar(n=10, m=5, foo=Foo(n=11)))
    except ValidationError as e:
        print(e)
    try:
        print(Bar.parse_obj({"n": 10, "m": 5, "foo": {"n": 11}}))
    except ValidationError as e:
        print(e)


def main():
    basic_validator()
    validator_with_pre()
    validator_with_multi_fields()


if __name__ == '__main__':
    main()
