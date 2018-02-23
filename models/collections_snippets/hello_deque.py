from collections import deque


def main():
    d = deque('ab')
    print(d)
    for elem in d:
        print(elem)
    d.append('c')
    print(d)
    print(d.pop())
    print(d.popleft())
    print(d)
    d.extend('def')
    d.extendleft('ghi')
    print(d)
    d = deque('jklmnop', 3)
    print(d)


if __name__ == '__main__':
    main()

