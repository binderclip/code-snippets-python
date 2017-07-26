# coding: utf-8


def main():
    d = {
        'foo': 'bar'
    }
    for k, v in d.items():
        print('<{}: {}>'.format(k, v))


if __name__ == '__main__':
    main()
