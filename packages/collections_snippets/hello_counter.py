# coding: utf-8
from collections import Counter


def main():
    cnt = Counter()
    for n in [1, 2, 3, 2, 1, 4, 7, 6, 2]:
        cnt[n] += 1
    print(cnt.items())
    print(cnt.most_common(10))


if __name__ == '__main__':
    main()
