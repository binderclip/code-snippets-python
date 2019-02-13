import math


def factorial(n):
    """
    Return the factorial of n, an exact integer >= 0.

    >>> factorial(1)
    1
    >>> factorial(2)
    2

    :param n:
    :return:
    """
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n+1 == n:  # catch a value like 1e300
        raise OverflowError("n too large")
    result = 1
    factor = 2
    while factor <= n:
        result *= factor
        factor += 1
    return result


def main():
    print(factorial(1))
    print(factorial(2))


if __name__ == '__main__':
    main()


# https://docs.python.org/2/library/doctest.html
