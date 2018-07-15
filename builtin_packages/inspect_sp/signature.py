import inspect


def foo(a, b: int) -> int:
    return int(a) + b


def main():
    foo(1, 10)
    sig = inspect.signature(foo)
    for name, parameter in sig.parameters.items():
        print(name, parameter, parameter.annotation)
    print(sig.return_annotation)


if __name__ == '__main__':
    main()
