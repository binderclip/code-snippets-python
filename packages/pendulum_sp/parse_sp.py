import pendulum


def main():
    dts = '2018-04-13 16:06:11.844265+08:00'
    dt = pendulum.parse(dts)
    print(dt)

    # without timezone
    dts = '2018-04-13 17:59:15'
    dt = pendulum.parse(dts)
    print(dt)

    # parse with timezone
    tz_shanghai = pendulum.timezone('Asia/Shanghai')

    dts = '2018-04-13 17:59:15'
    # dt = pendulum.parse(dts, tz='Asia/Shanghai')
    dt = pendulum.parse(dts, tz=tz_shanghai)
    print(dt)
    print(dt.in_tz(tz_shanghai))


    dts = '2018-04-13 17:59:15+00:00'
    dt = pendulum.parse(dts, tz='Asia/Shanghai')
    print(dt)
    print(dt.in_tz(tz_shanghai))


if __name__ == '__main__':
    main()
