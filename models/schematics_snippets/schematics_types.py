# coding: utf-8
import datetime
from schematics.models import Model
from schematics.types import StringType, IntType, DateTimeType, ModelType


class MyModel(Model):

    s = StringType()
    i = IntType()


def main():
    mm = MyModel({"s": "ss", "i": "1"})
    print(mm.to_primitive())


if __name__ == '__main__':
    main()
