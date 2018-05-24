import inspect



def f(a, b=1, *pos, **named):
    print('... in f')
    print(inspect.getcallargs(f, 2, 2, 2, 2))


def main():
    print(inspect.getcallargs(f, 1, 2, 3, 4))
    f('x')


if __name__ == '__main__':
    main()

