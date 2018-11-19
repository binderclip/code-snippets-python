from pydantic import BaseModel


class A(BaseModel):
    x: str = 'aaa'


class B(BaseModel):
    x: str = 'bbb'


class AA(BaseModel):
    x: str = 'aaa'
    y: A


class BB(BaseModel):
    x: str = 'bbb'
    y: A


def main():
    a = A()
    print(a)
    print(a.fields)
    # b = B(**a.fields)
    # pydantic.error_wrappers.ValidationError: 1 validation error
    # x
    #   str type expected (type=type_error.str)
    b = B(**a.dict())
    print(b)
    print('===')
    aa = AA(y=a)
    print(aa)
    print(a.fields)
    print(aa.dict())
    bb = BB(**aa.dict())
    print(bb)
    bb2 = BB.parse_obj(aa.dict())
    print(bb2)
    # bb3 = BB.parse_obj(aa)
    # pydantic.error_wrappers.ValidationError: 1 validation error
    # __obj__
    #   BB expected dict not AA (type=type_error)
    bb3 = BB.parse_obj({'x': 'bb3', 'y': A()})
    print(bb3)
    print(bb3.dict())


if __name__ == '__main__':
    main()
