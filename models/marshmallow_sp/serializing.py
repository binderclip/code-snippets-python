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
    def pre_load(self, data):
        print('>>> ue pre_load')
        print(data)
        return data

    @post_load
    def post_load(self, item):
        print('>>> ue post_load')
        print(item)
        return item

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
    def pre_load(self, item):
        print('>>> u pre_load')
        print(item)
        return item

    @post_load
    def post_load(self, data):
        print('>>> u post_load')
        print(data)
        return data

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

    print('=== dump dict ===')
    result = schema.dump({"name": "Monty", "data": {"age": 18, "foo": "bar"}})
    print(result)

    print('=== dump obj ===')
    user = User(name="Monty", data={"age": 18, "foo": "bar"})
    result = schema.dump(user)
    print(result)

    schema = UserSchema(many=True)
    print('=== dump dict many ===')
    result = schema.dump([
        {"name": "Monty", "data": {"age": 18, "foo": "bar"}},
        {"name": "Kin", "data": {"age": 28, "baz": "bar"}},
    ])
    print(result)


if __name__ == '__main__':
    main()
