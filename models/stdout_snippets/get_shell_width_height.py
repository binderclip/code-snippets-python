# coding: utf-8
import os


def get_shell_width_height():
    print('=== get_shell_width_height ===')
    print os.popen('stty size', 'r').read().split()
    rows, columns = os.popen('stty size', 'r').read().split()
    print('width: {}, height: {}'.format(columns, rows))


def main():
    get_shell_width_height()


if __name__ == '__main__':
    main()

# https://stackoverflow.com/questions/566746/how-to-get-linux-console-window-width-in-python
