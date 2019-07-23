from heapq import *


def main():
    h = []
    heappush(h, (5, 'write code'))
    heappush(h, (7, 'release product'))
    heappush(h, (1, 'write spec'))
    heappush(h, (3, 'create tests'))
    print(heappop(h))
    print(h)


if __name__ == '__main__':
    main()
