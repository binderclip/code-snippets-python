import datetime
import json


class MyEncoder(json.JSONEncoder):
    ENCODER_BY_TYPE = {
        datetime.datetime: lambda dt: dt.isoformat(),
        set: list,
    }

    def default(self, o):
        try:
            encoder = self.ENCODER_BY_TYPE[type(o)]
        except KeyError:
            return super().default(o)
        return encoder(o)


def main():
    data = {
        "my_dt": datetime.datetime.now(),
        "my_set": {1, 2, 3},
    }
    print(data)
    print(json.dumps(data, cls=MyEncoder))


if __name__ == '__main__':
    main()

# https://github.com/samuelcolvin/pydantic/issues/133
# https://github.com/tutorcruncher/socket-server/blob/master/tcsocket/app/utils.py#L16-L35
