import time


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print('{} ({}, {}) {} sec'.format(method.__name__, args, kw, te - ts))
        return result

    return timed


# build and return a list
def firstn_l(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums


# using the generator pattern (an iterable)
class firstn_c(object):
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()
    # 没有 __next__ 的话会报：TypeError: iter() returned non-iterator of type 'firstn_c'

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num + 1
            return cur
        else:
            raise StopIteration()


# a generator that yields items instead of returning a list
def firstn_g(n):
    num = 0
    while num < n:
        yield num
        num += 1


@timeit
def test_firstn_l(n):
    sum_of_first_n = sum(firstn_l(n))
    print(sum_of_first_n)


@timeit
def test_firstn_c(n):
    sum_of_first_n = sum(firstn_c(n))
    print(sum_of_first_n)


@timeit
def test_firstn_g(n):
    sum_of_first_n = sum(firstn_g(n))
    print(sum_of_first_n)


@timeit
def test_range(n):
    sum_of_first_n = sum(range(n))
    print(sum_of_first_n)


def test_generator_expression():
    print("=== test_generator_expression ===")
    doubles = (2 * n for n in range(50))
    print(type(doubles))

    doubles = [2 * n for n in range(50)]
    print(type(doubles))

    doubles = list(2 * n for n in range(50))
    print(type(doubles))



def main():
    # test_firstn_c(10000000)     # 5.15s
    # test_firstn_g(10000000)     # 1.11s
    # test_range(10000000)        # 0.21s

    # test_firstn_l(100000000)    # 17.53s，100M 数字，实际占用 2.xG 内存
    # test_firstn_g(100000000)    # 11.09s，几乎没有额外内存占用
    # test_firstn_l(1000000000)    # 327.57s，1G 数字，实际占用 37G 内存
    # test_firstn_g(1000000000)    # 110.77s，几乎没有额外内存占用

    # print(type(firstn_l(1)))
    # print(type(firstn_c(1)))
    # print(type(firstn_g(1)))

    test_generator_expression()


if __name__ == '__main__':
    main()
