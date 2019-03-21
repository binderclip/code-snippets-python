# coding: utf-8


def init_list():
    print("=== init_list ===")
    l = list()
    print(l)
    l2 = []
    print(l2)
    l3 = list((1, 2))
    print(l3)
    l4 = [1, 2]
    print(l4)


def insert_append_and_extend_list():
    print("=== insert_append_and_extend_list ===")
    l = ['e', 'h']
    l.insert(-1, 'g')
    print(l)
    l.insert(1, 'f')
    print(l)
    l.insert(0, 'd')
    print(l)
    l.insert(10, 'i')
    print(l)
    l.append('l')
    print(l)
    l.extend(['m', 'n'])
    print(l)
    l[0:0] = ['b', 'c']
    print(l)
    l = ['a'] + l
    print(l)


def remove_pop_list():
    print("=== remove_pop_list ===")
    l = ['a', 'b', 'c', 'd', 'e', 'e']
    print(l)
    print('l.remove: {}'.format(l.remove('e')))   # 只删除第一次出现的，没有返回
    print(l)
    # l.remove('h')   # 删除不存在的会导致 ValueError
    if 'h' in l:
        l.remove('h')
    l.pop()
    print(l)
    l.pop(1)
    print('l.pop: {}'.format(l.pop(1)))
    print(l)
    # l.pop(10)   # IndexError: pop index out of range


def get_len_count_index_list():
    print("=== get_len_count_index_list ===")
    l = ['a', 'b', 'c', 'd', 'e', 'e']
    print(l[0])
    # l[10] = 'z'    # IndexError: list index out of range
    # print(l[10])    # IndexError: list index out of range
    # print(l.get(10))    # 'list' object has no attribute 'get'
    print('len: {}'.format(len(l)))
    print('count d: {}'.format(l.count('d')))
    print('count e: {}'.format(l.count('e')))
    print('count f: {}'.format(l.count('f')))
    print('index d: {}'.format(l.index('d')))
    print('index e: {}'.format(l.index('e')))
    # print('index f: {}'.format(l.index('f')))   # ValueError: 'f' is not in list


def sort_reverse_list():
    print("=== sort_reverse_list ===")
    l = ['e', 'b', 'c', 'a', 'f', 'd']
    print(l)
    print(l.sort())     # return None
    print(l)
    l.sort(cmp=lambda x, y: -(cmp(x, y)))
    print(l)
    print(l.reverse())    # return None
    print(l)
    print(list(reversed(l)))    # return a reversed iterator
    print(l)


def _sort_func(x):
    return x[0] + x[1]


def sort_list():
    print("=== sort_list ===")
    l = [(1, 2), (3, 1), (2, 3)]
    print(sorted(l, key=lambda x: x[1]))
    print(sorted(l, key=lambda x: x[0]))
    print(sorted(l, key=_sort_func))


def list_index():
    print("=== list_index ===")
    l = ['a', 'b', 'c']
    print(l.index('a'))


def list_slice():
    print("=== list_slice ===")
    l = [1, 2, 3]
    print(l[:1])
    print(l[:5])
    print(l[-1:])
    print(l[-5:])
    print(l[:-1])
    print(l[10:20])


def list_slice_with_step():
    print("=== list_slice_with_step ===")
    l = list(range(20))
    print(l[::3])
    print(l[1::3])
    print(l[2::3])
    print(l[::-1])
    l[::3] = [0, 0, 0, 0, 0, 0, 0]
    print(l)
    del l[::3]
    print(l)



def list_comprehension():
    print("=== list_comprehension ===")
    # 列表推导式
    l = [i * i for i in range(3)]
    print(l)


def test_insert_when_traversing():
    print("=== test_insert_when_traversing ===")
    l = [3, 4]
    for i in l:
        l.insert(0, -i)
        print(i)
    # 会停不下来


def main():
    # init_list()
    # insert_append_and_extend_list()
    # remove_pop_list()
    # get_len_count_index_list()
    # sort_reverse_list()
    sort_list()
    # list_index()
    # list_slice()
    # list_slice_with_step()
    # list_comprehension()
    # test_insert_when_traversing()


if __name__ == '__main__':
    main()

# https://www.tutorialspoint.com/python/python_lists.htm
# https://stackoverflow.com/a/9028088/3936457
# https://stackoverflow.com/questions/8785554/how-do-i-insert-a-list-at-the-front-of-another-list
