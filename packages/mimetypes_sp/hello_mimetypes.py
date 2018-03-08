import mimetypes


def main():
    print(mimetypes.guess_type('xxx.png'))
    print(mimetypes.guess_type('xxx.txt'))
    print(mimetypes.guess_type('png'))


if __name__ == '__main__':
    main()


# https://docs.python.org/3/library/mimetypes.html
