
def printer():
    print('>>> printer start')
    counter = 0
    while True:
        print('>>> in while')
        string = yield
        print('[{0}] {1}'.format(counter, string))
        counter += 1


def test_printer():
    p = printer()
    print(">>> let's next")
    next(p)
    # 如果不 next 就直接 send 的话 TypeError: can't send non-None value to a just-started generator
    print(">>> send hi")
    p.send('Hi')
    print(">>> send my...")
    p.send('My name is hsfzxjy.')
    print(">>> send bye")
    p.send('Bye')
    print(">>> send bye!")
    p.send('bye!')


def main():
    test_printer()


if __name__ == '__main__':
    main()
