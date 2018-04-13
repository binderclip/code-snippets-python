import time
import datetime


def main():
    print(time.timezone)
    print(time.tzname)
    print(time.localtime())
    print(time.localtime().tm_isdst)
    print(time.altzone)
    utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
    utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
    print(datetime.timezone(offset=utc_offset))


if __name__ == '__main__':
    main()
