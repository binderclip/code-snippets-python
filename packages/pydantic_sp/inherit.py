from pydantic import BaseModel


class A(BaseModel):
    a: str = 'aaa'


class B(BaseModel):
    b: str = 'bbb'


class AB(A, B):
    ab: str = 'aaabbb'


def main():
    print(AB())


if __name__ == '__main__':
    main()
