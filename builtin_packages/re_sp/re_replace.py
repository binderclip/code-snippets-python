import re


def main():
    s = 'abc x123 def'
    s2 = re.sub('x', 'y', s)
    print(s)
    print(s2)


if __name__ == '__main__':
    main()
