import random


def test_randrange():
    print('=== test_randrange ===')
    s = ''
    for i in range(100):
        s += '{} '.format(random.randrange(5))
    print(s)

    s = ''
    for i in range(100):
        s += '{} '.format(random.randrange(start=1, stop=3, step=1))
    print(s)


def test_sample():
    print('=== test_sample ===')
    l = range(1, 5)
    s = ''
    for i in range(100):
        s += '{} '.format(random.sample(l, 2))
    print(s)


def test_random():
    print('=== test_random ===')
    s = ''
    for i in range(100):
        s += '{} '.format(random.random())
    print(s)


def test_uniform():
    print('=== test_uniform ===')
    s = ''
    for i in range(100):
        s += '{} '.format(random.uniform(1.0, 1.2))
    print(s)


def test_randint():
    print('=== test_randint ===')
    s = ''
    for i in range(100):
        s += '{} '.format(random.randint(1, 4))
    print(s)


def test_getrandbits():
    print('=== test_getrandbits ===')
    print("{0:064b}".format(2 ** 60 - 1))
    print("{0:064b}".format(random.getrandbits(60)))


def main():
    # random.seed(1)  # test seed

    test_randrange()
    test_sample()
    test_random()
    test_uniform()
    test_randint()
    test_getrandbits()


if __name__ == '__main__':
    main()
