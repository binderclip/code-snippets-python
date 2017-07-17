# coding: utf-8


def init_set():
    print("===== init_set =====")
    s = set()
    print(s)
    s2 = set([])
    print(s2)
    s3 = set([1])
    print(s3)


def union_add_intersection():
    s = set([1, 2, 3])
    s2 = set([2, 3, 4])
    print(s.intersection(s2))
    print(s)
    print(s.union(s2))
    print(s)


def main():
    init_set()
    union_add_intersection()

if __name__ == '__main__':
    main()
