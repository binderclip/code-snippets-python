# coding: utf-8


def write_and_read():
    print("=== write_and_read ===")
    with open('temp.txt', 'w') as f:
        f.write('hello\nworld')
    with open('temp.txt', 'r') as f:
        lines = f.readlines()
        print('Lines:\n{}'.format(lines))


def write_with_line_break_and_read():
    print("=== write_with_line_break_and_read ===")
    lines = ['hello', 'world']
    with open('temp.txt', 'w') as f:
        f.writelines(line + '\n' for line in lines)
    with open('temp.txt', 'r') as f:
        lines = f.readlines()
        print('Lines:\n{}'.format(lines))


def main():
    write_and_read()
    write_with_line_break_and_read()


if __name__ == '__main__':
    main()

# https://www.guru99.com/reading-and-writing-files-in-python.html
