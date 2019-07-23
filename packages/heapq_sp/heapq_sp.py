from heapq import *


def main():
    h = []  # 毕竟 heap 是可以用 list 实现的，所以这个 heapq 直接用 list 操作也没毛病
    # 不确定有没有初始化的过程，以及中间强行破坏后会怎么样
    heappush(h, (5, 'write code'))
    heappush(h, (7, 'release product'))
    heappush(h, (1, 'write spec'))
    heappush(h, (3, 'create tests'))
    print(heappop(h))
    print(h)


if __name__ == '__main__':
    main()
