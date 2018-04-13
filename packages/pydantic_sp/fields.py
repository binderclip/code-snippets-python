import datetime
from pydantic import BaseModel


class MyModel(BaseModel):
    dt: datetime.datetime


def main():
    model = MyModel.parse_obj({
        "dt": "2018-04-13 17:42:42"
    })
    print(model.dt)

    model = MyModel.parse_obj({
        "dt": "2018-04-13 16:06:11.844265+08:00"
    })
    print(model.dt)


if __name__ == '__main__':
    main()
