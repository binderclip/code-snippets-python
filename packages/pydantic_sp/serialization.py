import json
import datetime
from pydantic import BaseModel


class Model(BaseModel):
    foo: int
    bar: str
    baz: datetime.datetime = None


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


def test_model_and_json():
    print('=== test_model_and_json ===')
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


def test_none_field():
    print('=== test_none_field ===')
    m = Model(foo=1, bar='r')
    d = m.dict()
    print(d)


def main():
    test_model_and_json()
    test_none_field()


if __name__ == '__main__':
    main()
