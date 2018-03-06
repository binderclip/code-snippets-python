# coding: utf-8
from schematics.models import Model
from schematics.types import ListType, StringType, ModelType


# list of string
# list of model


class A(Model):
    s = StringType()


class B(Model):
    sl = ListType(StringType)
    ml = ListType(ModelType(A))


def main():
    b = B()
    b.sl = ["ee", "ff"]
    b.ml = [A({"s": "ss"}), A({"s": "sss"})]
    print(b.serialize())


if __name__ == '__main__':
    main()
