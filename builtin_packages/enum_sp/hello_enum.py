from enum import Enum, IntEnum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Color2(IntEnum):
    RED = 1
    GREEN = 2
    BLUE = 3


def main():
    c_r = Color.RED
    print(c_r)
    print(c_r.name)
    print(c_r.value)
    # print(int(c_r))   # TypeError: int() argument must be a string, a bytes-like object or a number, not 'Color'

    c_r = Color2.RED
    print(c_r)
    print(c_r.name)
    print(c_r.value)
    print(int(c_r))
    print(c_r.__dict__)


if __name__ == '__main__':
    main()
