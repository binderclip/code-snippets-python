import time
import datetime


def main():
    dt = datetime.datetime.now()
    print(dt.timestamp())
    print(time.time())


if __name__ == '__main__':
    main()
