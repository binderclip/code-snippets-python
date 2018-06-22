from pydantic import BaseModel
from typing import List


class Foo(BaseModel):
    bar: List[str] = []


def main():
    foo1 = Foo()
    foo1.bar.append('a')
    print(foo1)

    foo2 = Foo()
    foo2.bar.append('b')
    print(foo2)


if __name__ == '__main__':
    main()
