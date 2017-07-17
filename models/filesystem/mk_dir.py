# coding: utf-8
import os


def main():
    dir_path = 'temp_dir'
    print('dir <{}> exists: {}'.format(dir_path, os.path.exists(dir_path)))
    try:
        os.mkdir(dir_path)
    except OSError as e:
        print(e)


if __name__ == '__main__':
    main()
