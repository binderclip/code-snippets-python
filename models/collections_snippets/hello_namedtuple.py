# coding: utf-8
from collections import namedtuple
User = namedtuple('User', ['name', 'sex', 'age'])


def main():
    u1 = User(name='foo', sex='male', age=21)
    u2 = User._make(['bar', 'female', 23])
    print(u1)
    print(u1.name, u1.sex, u1.age)
    for t in u1:
        print(t)
    print(u2)
    u1._replace(age=22)
    print(u1)
    print(u1._asdict())


if __name__ == '__main__':
    main()
