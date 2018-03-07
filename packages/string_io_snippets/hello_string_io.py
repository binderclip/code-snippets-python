import io


def use_as_file():
    print('=== use_as_file ===')
    text = 'hello world!'
    f = io.StringIO()
    f.write(text)
    f.seek(0)
    print(f)
    # print(f.name)  # AttributeError: '_io.StringIO' object has no attribute 'name'
    f.name = 'hello.txt'
    print(f)
    print(f.name)
    print(f.read())
    f.close()


def use_as_stream():
    print('=== use_as_stream ===')
    f = io.StringIO("some initial text data")
    print(f.read())
    f.close()


def main():
    use_as_file()
    use_as_stream()


if __name__ == '__main__':
    main()
