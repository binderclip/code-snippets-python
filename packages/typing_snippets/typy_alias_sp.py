# coding: utf-8
from typing import List, Tuple, Dict

Vector = List[float]

ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]


def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


def broadcast_message1(message: str, servers: List[Server]) -> None:
    print(message, '->')
    for server in servers:
        print(server)


def broadcast_message2(
        message: str,
        servers: List[Tuple[Tuple[str, int], Dict[str, str]]]) -> None:
    print(message, '->')
    for server in servers:
        print(server)


def main():
    new_vector = scale(2.0, [1.0, -4.2, 5.4])
    print(new_vector)

    broadcast_message1('hello 1', [(("abc.com", 80), {"foo": "bar"})])
    broadcast_message2('hello 2', [(("xyz.com", 443), {"bar": "baz"})])


if __name__ == '__main__':
    main()
