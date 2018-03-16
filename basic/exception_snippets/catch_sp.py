

def int_it(s):
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print(e)


def main():
    int_it(None)
    int_it('hello')


if __name__ == '__main__':
    main()
