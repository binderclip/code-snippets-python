import io


def main():
    f = io.BytesIO(b"some initial binary data: \x00\x01")
    print(f.read())
    f.close()


if __name__ == '__main__':
    main()
