# coding: utf-8


def main():
    d1 = {"a": 1}
    d1_1 = {"a": 1}
    d2 = {"l": [1, 2, 3]}
    d2_1 = {"l": [1, 2, 3]}
    d3 = {"d": {"i": 1}}
    d3_1 = {"d": {"i": 1}}
    d3_2 = {"d": {"i": 1}, "i": 2}
    print(d1 == d1_1)
    print(d2 == d2_1)
    print(d3 == d3_1)
    print(d3 == d3_2)


if __name__ == '__main__':
    main()
