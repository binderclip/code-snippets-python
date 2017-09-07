# coding: utf-8


def print_kwargs(**kwargs):
    print("=== print_kwargs ===")
    print(kwargs)


def main():
    print_kwargs(a="aa", b="bb")
    print_kwargs(**{"c": "cc", "d": "dd"})


if __name__ == '__main__':
    main()
