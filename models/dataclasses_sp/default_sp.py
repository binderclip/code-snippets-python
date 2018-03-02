from dataclasses import dataclass


@dataclass
class C:
    x: int
    y: int
    z: int = 10
    # t: int      # TypeError: non-default argument 't' follows default argument


def main():
    c = C(1, 2)
    print(c)
    # c = C(1)    # TypeError: __init__() missing 1 required positional argument: 'y'


if __name__ == '__main__':
    main()
