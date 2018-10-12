import math
import datetime
from typing import List


def datetime_range(
            start_time: datetime.datetime,
            end_time: datetime.datetime,
            step: datetime.timedelta
        ) -> List[datetime.datetime]:
    step_seconds = step.total_seconds()
    return [start_time + datetime.timedelta(seconds=x * step_seconds)
            for x in range(math.ceil((end_time - start_time).total_seconds() / step_seconds))]


def datetime_pairs(start_time, end_time, step):
    dts = datetime_range(start_time, end_time, step)
    for i, dt in enumerate(dts):
        yield dt, dts[i + 1] if i + 1 < len(dts) else end_time


def main():
    start_time = datetime.datetime(2018, 3, 28, 22)
    end_time = datetime.datetime(2018, 3, 29, 0, 30)

    print(datetime_range(start_time, end_time, datetime.timedelta(hours=1)))
    print(list(datetime_pairs(start_time, end_time, datetime.timedelta(hours=1))))

    start_time = datetime.datetime(2018, 3, 27)
    end_time = datetime.datetime(2018, 3, 29)

    print(datetime_range(start_time, end_time, datetime.timedelta(days=1)))
    print(list(datetime_pairs(start_time, end_time, datetime.timedelta(days=1))))


if __name__ == '__main__':
    main()
