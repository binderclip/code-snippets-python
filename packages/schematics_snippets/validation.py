from schematics.models import Model
from schematics.types import StringType, IntType
from schematics.exceptions import DataError


class MyModel1(Model):
    foo = StringType()


class MyModel2(Model):
    foo = StringType(required=True)


class MyModel3(Model):
    foo = IntType()


def validate_model(m):
    try:
        m.validate()
    except DataError as e:
        print(e)
        print(e.messages)


def main():
    m1 = MyModel1({'foo': 'a'})
    m1.validate()

    m2 = MyModel1({})
    m2.validate()

    m3 = MyModel2({})
    # m3.validate()   # schematics.exceptions.DataError: {"foo": ["This field is required."]}
    validate_model(m3)

    m4 = MyModel3({'foo': '4'})
    print(m4, m4.foo)
    validate_model(m4)


if __name__ == '__main__':
    main()
