import bisect


def reverse_bisect_right(a, x, lo=0, hi=None):
    """Return the index where to insert item x in list a, assuming a is sorted in descending order.

    The return value i is such that all e in a[:i] have e >= x, and all e in
    a[i:] have e < x.  So if x already appears in the list, a.insert(x) will
    insert just after the rightmost x already there.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.

    Essentially, the function returns number of elements in a which are >= than x.
    >>> a = [8, 6, 5, 4, 2]
    >>> reverse_bisect_right(a, 5)
    3
    >>> a[:reverse_bisect_right(a, 5)]
    [8, 6, 5]
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x > a[mid]: hi = mid
        else: lo = mid+1
    return lo


def main():
    # asc
    print('=== asc ===')
    l = [1, 3, 5]
    print(bisect.bisect_left(l, 2))
    print(bisect.bisect_left(l, 3))
    print(bisect.bisect_left(l, 4))
    print(bisect.bisect_left(l, 7))
    print(bisect.bisect_right(l, 2))
    print(bisect.bisect_right(l, 3))
    print(bisect.bisect_right(l, 4))
    print(bisect.bisect_right(l, 7))
    # desc
    print('=== desc ===')
    l = [5, 3, 1]
    print(reverse_bisect_right(l, 2))
    print(reverse_bisect_right(l, 3))
    print(reverse_bisect_right(l, 4))
    print(reverse_bisect_right(l, 7))


if __name__ == '__main__':
    main()


# https://stackoverflow.com/questions/2591159/find-next-lower-item-in-a-sorted-list
# https://stackoverflow.com/questions/2247394/python-bisect-it-is-possible-to-work-with-descending-sorted-lists
