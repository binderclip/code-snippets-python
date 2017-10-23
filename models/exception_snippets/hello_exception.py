# coding: utf-8


def maybe_error(n, raise_it=False):
    print('maybe_error == start ==')
    a = None
    try:
        a = 10 / n
    except Exception as e:
        print('maybe_error == except ==')
        print('e: {}'.format(e))
        if raise_it:
            print('maybe_error == raise ==')
            raise e
    else:
        print('maybe_error == else ==')
    print('a = {}'.format(a))
    print('maybe_error == end ==')


def box(n, raise_it):
    try:
        maybe_error(n, raise_it)
    except Exception:
        pass


def main():
    box(1, raise_it=False)
    box(0, raise_it=False)
    box(0, raise_it=True)


if __name__ == '__main__':
    main()
