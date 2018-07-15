def init_set():
    print("===== init_set =====")
    s = set()
    print(s)
    s2 = set([])
    print(s2)
    s3 = {1}
    print(s3)


def union_operation():
    print("===== union_operation =====")
    s = {1, 2, 3}
    s2 = {2, 3, 4}
    print(s.intersection(s2))
    print(s)
    print(s.union(s2))
    print(s)
    print(s.update(s2))
    print(s)
    print(s - s2)

    l2 = [3, 4, 5]
    print(s.union(l2))
    s.update(l2)
    print(s)
    s.update(6)
    print(s)


def add_remove():
    print("===== set_add_remove =====")
    s = {1, 2, 3}
    s.add(4)
    s.remove(1)
    # s.remove(11)    # KeyError: 11
    if 11 in s:
        s.remove(11)
    print(s)
    print(s.pop())
    print(s)


def main():
    init_set()
    union_operation()
    add_remove()


if __name__ == '__main__':
    main()
