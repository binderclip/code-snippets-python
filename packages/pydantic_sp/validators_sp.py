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


def main():
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

    next_cursor = IntNextCursorDTO(cursor='Mg==', size='10')
    print(next_cursor)


if __name__ == '__main__':
    main()
