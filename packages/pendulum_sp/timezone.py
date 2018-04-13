import pendulum


def main():
    now = pendulum.now()
    print(now.tz, now.timezone, now.timezone_name, now.tzinfo)
    print(now)

    tz_shanghai = pendulum.timezone('Asia/Shanghai')
    print(now.in_tz(tz_shanghai))

    tz_utc = pendulum.timezone('UTC')
    print(now.in_tz(tz_utc))

    dts = "2018-04-13T10:13:37.225416+00:00"
    dt = pendulum.parse(dts)
    dt = dt.in_tz(tz_shanghai)
    print(dt)


if __name__ == '__main__':
    main()
