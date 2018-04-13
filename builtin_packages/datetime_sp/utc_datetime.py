import time
import datetime


def main():
    local_now = datetime.datetime.now()
    print(local_now)
    print(local_now.isoformat())

    utc_now = datetime.datetime.utcnow()
    print(utc_now)
    print(utc_now.isoformat())

    # calculate the offset taking into account daylight saving time
    utc_offset_sec = time.altzone if time.localtime().tm_isdst else time.timezone
    utc_offset = datetime.timedelta(seconds=-utc_offset_sec)
    timezone = datetime.timezone(offset=utc_offset)
    print(timezone)

    local_now_with_tz = datetime.datetime.now().replace(tzinfo=timezone)
    print(local_now_with_tz)
    print(local_now_with_tz.isoformat())

    utc_now_with_tz = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
    print(utc_now_with_tz)
    print(utc_now_with_tz.isoformat())


if __name__ == '__main__':
    main()


# https://stackoverflow.com/a/28147286/3936457
