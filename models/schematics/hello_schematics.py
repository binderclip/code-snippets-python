# coding: utf-8
from schematics.models import Model
from schematics.types import StringType


class HelloSchematics(Model):

    foo = StringType()


if __name__ == '__main__':
    hello_schematics = HelloSchematics({'foo': 'bar'})
    print(hello_schematics.serialize())

