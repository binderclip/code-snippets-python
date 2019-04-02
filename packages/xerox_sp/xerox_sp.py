import random

import xerox


def main():
    i = random.randint(0, 100)
    xerox.copy(str(i))
    print(i)
    print(xerox.paste())


if __name__ == '__main__':
    main()
