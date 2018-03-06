# coding: utf-8
import os


def get_file_dir_path():
    return os.path.dirname(os.path.realpath(__file__))


def join_path(path_a, path_b):
    return os.path.join(path_a, path_b)


def main():
    path_a = get_file_dir_path()
    path_b = "../common_text/foo.txt"
    path_ab = join_path(path_a, path_b)
    print('"{}" + "{}" = "{}"'.format(path_a, path_b, path_ab))
    with open(path_ab) as f:
        print(f.read())


if __name__ == '__main__':
    main()
