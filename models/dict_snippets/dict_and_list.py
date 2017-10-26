# coding: utf-8


def from_list_to_dict():
    print('=== from_list_to_dict ===')
    l = [('a', 'aa'), ('c', 'cc'), ('b', 'bb'), ('a', 'aaa')]
    d = dict(l)
    print(d)
    # l2 = ['a', 'c', 'b']
    # d2 = dict(l2)     # ValueError: dictionary update sequence element #0 has length 1; 2 is required


def from_dict_to_list():
    print('=== from_dict_to_list ===')
    d = {'a': 'aa', 'c': 'cc', 'b': 'bb'}
    print(list(d))
    print(list(d.keys()))
    print(list(d.values()))
    print(list(d.items()))


def change_dict_in_list():
    print('=== change_dict_in_list ===')
    l = [
        {
            "a": "1",
        },
        {
            "a": "2",
        }
    ]
    print(l)
    for d in l:
        d['b'] = d['a']
    print(l)


def main():
    from_list_to_dict()
    from_dict_to_list()
    change_dict_in_list()


if __name__ == '__main__':
    main()
