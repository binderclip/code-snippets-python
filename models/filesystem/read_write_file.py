# coding: utf-8


def main():
    with open('temp.txt', 'w') as f:
        f.writelines('Hello\nWorld')
    with open('temp.txt', 'r') as f:
        lines = f.readlines()
        print('Lines:\n{}'.format(lines))


if __name__ == '__main__':
    main()
