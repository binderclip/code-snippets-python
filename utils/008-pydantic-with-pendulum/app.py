import datetime
import pendulum
from pydantic import BaseModel


class MyDatetime(datetime.datetime):

    @classmethod
    def get_validators(cls):
        yield cls.parse_to_cst_local_datetime

    @classmethod
    def parse_to_cst_local_datetime(cls, dt):
        tz_shanghai = pendulum.timezone('Asia/Shanghai')
        # 默认使用 +8 时区
        if isinstance(dt, datetime.datetime):
            dt = pendulum.instance(dt, tz=tz_shanghai)
        else:
            dt = pendulum.parse(dt, tz=tz_shanghai)
        dt = dt.in_tz(tz_shanghai)
        return cls(
            year=dt.year,
            month=dt.month,
            day=dt.day,
            hour=dt.hour,
            minute=dt.minute,
            second=dt.second,
            microsecond=dt.microsecond,
        )


class MyModel(BaseModel):
    dt: MyDatetime


def main():
    model = MyModel.parse_obj({
        "dt": "2018-04-13 17:42:42"
    })
    print(model.dt)

    model = MyModel.parse_obj({
        "dt": "2018-04-13 16:06:11.844265+08:00"
    })
    print(model.dt)

    model = MyModel.parse_obj({
        "dt": "2018-04-13 16:06:11.844265+07:00"
    })
    print(model.dt)
    print(type(model.dt))

    model = MyModel.parse_obj({
        "dt": datetime.datetime.now()
    })
    print(model.dt)
    print(type(model.dt))


if __name__ == '__main__':
    main()
