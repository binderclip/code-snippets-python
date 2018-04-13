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
    dts = '2018-04-13 17:59:15'
    dt = pendulum.parse(dts, tz='Asia/Shanghai')
    print(dt)


if __name__ == '__main__':
    main()
