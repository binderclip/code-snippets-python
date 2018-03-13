import os
import tempfile


def main():
    tempdir = tempfile.gettempdir()
    print(os.path.join(tempdir, 'xxxx.txt'))


if __name__ == '__main__':
    main()
