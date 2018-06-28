import datetime


def main():
    dt1 = datetime.datetime(2018, 6, 27)
    dt2 = datetime.datetime(2018, 6, 28)
    print('max: {}'.format(max(dt1, dt2)))
    print('minus: {}'.format(dt1 - dt2))
    # print('plus: {}'.format(dt1 + dt2))       # TypeError: unsupported operand type(s) for +: 'datetime.datetime' and 'datetime.datetime'


if __name__ == '__main__':
    main()
