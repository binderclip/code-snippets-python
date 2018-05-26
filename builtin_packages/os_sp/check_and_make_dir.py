import os


def make_dir_if_not_exists(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def main():
    make_dir_if_not_exists('hello/world')


if __name__ == '__main__':
    main()
