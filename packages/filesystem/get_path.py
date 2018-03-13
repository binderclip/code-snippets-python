# coding: utf-8
import os


def get_file_path():
    return os.path.realpath(__file__)


def get_file_dir_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_file_name():
    return os.path.basename(get_file_path())


def get_cwd():
    return os.getcwd()


def get_home_path():
    home = os.path.expanduser("~")
    return home


def main():
    print('__file__ >>> {}'.format(__file__))
    print('file path >>> {}'.format(get_file_path()))
    print('dir path >>> {}'.format(get_file_dir_path()))
    print('file name >>> {}'.format(get_file_name()))
    print('cwd >>> {}'.format(get_cwd()))
    print('home >>> {}'.format(get_home_path()))

if __name__ == '__main__':
    main()
