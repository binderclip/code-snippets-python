import datetime


def main():
    now = datetime.datetime.now()
    print(now)
    print(now.strftime('%Y-%m-%d %H:%M:%S.%f'))


if __name__ == '__main__':
    main()
