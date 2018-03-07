import io


def main():
    text = 'hello world!'
    with io.StringIO() as f:
        f.write(text)
        f.seek(0)
        f.name = 'hello.txt'
        print(f)
        print(f.name)
        print(f.read())


if __name__ == '__main__':
    main()
