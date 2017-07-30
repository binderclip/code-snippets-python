# coding: utf-8


class Config(object):
    FOO = 'bar'


def main():
    print('Config.FOO: {}'.format(Config.FOO))


if __name__ == '__main__':
    main()
