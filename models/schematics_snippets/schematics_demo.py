# coding: utf-8
from schematics.models import Model
from schematics.types import StringType, IntType


class HelloSchematics(Model):

    foo = StringType()


class MyDefault(Model):

    s1 = StringType()
    s2 = StringType(default="")
    s3 = StringType(default="x")

    i1 = IntType()
    i2 = IntType(default=0)
    i3 = IntType(default=1)


def hello():
    print("=== hello ===")
    hello_schematics = HelloSchematics({'foo': 'bar'})
    print(hello_schematics.serialize())
    print(hello_schematics.to_native())


def default_value():
    print("=== my_default ===")
    my_default = MyDefault()
    print(my_default.serialize())
    print(my_default.to_native())


def main():
    hello()
    default_value()


if __name__ == '__main__':
    main()

