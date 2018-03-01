import fire


def say_hello(name):
    print(f'hello {name}')


if __name__ == '__main__':
    fire.Fire(say_hello)
