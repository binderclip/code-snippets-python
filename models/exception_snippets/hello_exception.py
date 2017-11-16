# coding: utf-8


def maybe_error(n, raise_it=False):
    print('maybe_error == start == {}'.format(n))
    a = None
    try:
        a = 10 / n
    except Exception as e:
        print('maybe_error == except == {}'.format(n))
        print('e: {}'.format(e))
        if raise_it:
            print('maybe_error == raise == {}'.format(n))
            raise e
    else:
        print('maybe_error == else == {}'.format(n))
    finally:
        print('maybe_error == finally == {}'.format(n))
    print('maybe_error == end == {}'.format(n))


def box(n, raise_it):
    try:
        maybe_error(n, raise_it)
    except Exception:
        print('box == except == {}'.format(n))


def main():
    box(1, raise_it=False)
    box(0, raise_it=False)
    box(0, raise_it=True)


if __name__ == '__main__':
    main()
