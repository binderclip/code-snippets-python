# coding: utf-8


def main():
    start = 1
    end = 10
    step = 1

    for i in xrange(start, end + step, step):
        print("{:02d}".format(i))   # 01


if __name__ == '__main__':
    main()
