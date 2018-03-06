import datetime
from marshmallow import Schema, fields, post_load, ValidationError,\
    validates_schema, validates


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return f'User(name={self.name!r})>'


class UserSchema(Schema):
    name = fields.Str(validate=lambda s: 'admin' not in s)
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data):
        return User(**data)


# === validate ===

def validate_quantity(n):
    if n < 0:
        raise ValidationError('Quantity must be greater than 0.')


class ItemSchema(Schema):
    quantity = fields.Integer(validate=[validate_quantity])

    @validates('quantity')
    def validate_quantity2(self, value):
        if value > 30:
            raise ValidationError('Quantity must not be greater than 30.')


class NumberSchema(Schema):
    field_a = fields.Integer()
    field_b = fields.Integer()

    @validates_schema
    def validate_numbers(self, data):
        if data['field_b'] >= data['field_a']:
            raise ValidationError('field_a must be greater than field_b')


class UserSchema2(Schema):
    name = fields.String(required=True)
    age = fields.Integer(
        required=True,
        error_messages={'required': 'Age is required.'}
    )
    city = fields.String(
        required=True,
        error_messages={'required': {'message': 'City required', 'code': 400}}
    )
    email = fields.Email()


def main():
    # === dump ===
    user = User(name='Monty', email='monty@python.org')

    schema = UserSchema()
    result = schema.dump(user)
    print(result)
    json_result = schema.dumps(user)
    print(json_result)

    summary_schema = UserSchema(only=('name', 'email'))
    result = summary_schema.dump(user)
    print(result)
    # === end dump ===
    # === load ===
    user_data = {
        # 'created_at': '2014-08-11T05:26:03.869245',
        'email': u'ken@yahoo.com',
        'name': u'Ken'
    }
    schema = UserSchema()
    result = schema.load(user_data)
    print(result)
    # === end load ===
    # === collections of objects ===
    user1 = User(name="Mick", email="mick@stones.com")
    user2 = User(name="Keith", email="keith@stones.com")
    users = [user1, user2]
    schema = UserSchema(many=True)
    result = schema.dump(users)  # OR UserSchema().dump(users, many=True)
    print(result)
    # result = schema.dump(user1)  # TypeError: 'User' object is not iterable
    # === end collections of objects ===
    # === validation ===
    result = UserSchema().load({'name': 'John', 'email': 1})
    print(result.errors)
    print(result.data)

    result = UserSchema().load({'name': 'admin'})
    print(result.errors)
    print(result.data)

    in_data = {'quantity': 31}
    result = ItemSchema().load(in_data)
    print(result.errors)
    print(result.data)

    schema = NumberSchema()
    result = schema.load({'field_a': 1, 'field_b': 2})
    print(result.errors)
    print(result.data)

    result = UserSchema2().load({'email': 'foo@bar.com'})
    print(result.errors)
    print(result.data)

    result = UserSchema2().load({'age': 42}, partial=('name',))
    print(result.errors)
    print(result.data)

    result = UserSchema2().load({'age': 42}, partial=True)
    print(result.errors)
    print(result.data)

    errors = UserSchema2().validate({'email': 'foo@bar.com'})
    print(errors)
    # === end validation ===


if __name__ == '__main__':
    main()
