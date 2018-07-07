class CustomOpen(object):
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        self.file.close()


def main():
    with CustomOpen('test_file') as f:
        # a = 1 / 0
        contents = f.read(1000)
        print(contents)


if __name__ == '__main__':
    main()
