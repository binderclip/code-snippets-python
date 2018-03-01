import datetime
from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(missing=None)
    name = fields.Str()
    created_at = fields.DateTime(missing=lambda: str(datetime.datetime.now()))


def main():
    print(UserSchema().load({}))


if __name__ == '__main__':
    main()
