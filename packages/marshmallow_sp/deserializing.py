import json
from marshmallow import Schema, fields, pre_load, post_load, pre_dump, post_dump


class User(object):
    def __init__(self, name, data={}):
        self.name = name
        self.data = json.dumps(data)

    def __repr__(self):
        return f'User(name={self.name}, data={repr(self.data)})'

    def __str__(self):
        return self.__repr__()


class UserExtraSchema(Schema):
    age = fields.Int()

    @pre_load
    def pre_load(self, item):
        print('>>> ue pre_load')
        print(item)
        return item

    @post_load
    def post_load(self, data):
        print('>>> ue post_load')
        print(data)
        return data

    @pre_dump
    def pre_dump(self, item):
        print('>>> ue pre_dump')
        if isinstance(item, str):
            return json.loads(item)
        return item

    @post_dump
    def post_dump(self, data):
        print('>>> ue post_dump')
        print(data)
        return data


class UserSchema(Schema):
    name = fields.Str(validate=lambda s: 'admin' not in s)
    extra = fields.Nested(UserExtraSchema(), attribute="data")

    @pre_load
    def pre_load(self, data):
        print('>>> u pre_load')
        print(data)
        return data

    @post_load
    def post_load(self, item):
        print('>>> u post_load')
        print(item)
        return User(**item)

    @pre_dump
    def pre_dump(self, item):
        print('>>> u pre_dump')
        print(item)
        return item

    @post_dump
    def post_dump(self, data):
        print('>>> u post_dump')
        print(data)
        return data


def main():
    schema = UserSchema()

    print('=== load dict ===')
    result = schema.load({"name": "Monty", "extra": {"age": 18, "foo": "bar"}})
    print(result)


if __name__ == '__main__':
    main()
