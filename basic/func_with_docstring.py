
def hello(name, times=1):
    """say hello to x, y times
    :param name: name to say greeting
    :param times: say hello how many times
    :type name: str
    :type times: int
    :return: the whole greeting str
    :rtype: str
    """
    hs = 'hello ' * times
    return f'{hs}{name}!'


def main():
    s = hello('foo', 3)
    print(s)


if __name__ == '__main__':
    main()
