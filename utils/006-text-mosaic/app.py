def text_mosaic(text):
    if len(text) < 2:
        return text
    else:
        return text[0] * len(text)


def main():
    print(text_mosaic('8d175a93'))
    print(text_mosaic('08e235d012aa'))


if __name__ == '__main__':
    main()
