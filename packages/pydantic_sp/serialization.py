import json
import datetime
from pydantic import BaseModel


class Model(BaseModel):
    foo: int
    bar: str
    baz: datetime.datetime


class MyEncoder(json.JSONEncoder):
    ENCODER_BY_TYPE = {
        datetime.datetime: lambda d: d.strftime('%Y-%m-%d %H:%M:%S'),
        set: list,
    }

    def default(self, o):
        try:
            encoder = self.ENCODER_BY_TYPE[type(o)]
        except KeyError:
            return super().default(o)
        return encoder(o)


def main():
    m = Model(foo=1, bar='r', baz=datetime.datetime.now())
    print(m)
    d = m.dict()
    print(d)
    d = m.dict(exclude={'foo'})
    print(d)
    s = json.dumps(d, cls=MyEncoder)
    print(s)
    d = json.loads(s)
    d['foo'] = 2
    m = Model.parse_obj(d)
    print(m)


if __name__ == '__main__':
    main()
