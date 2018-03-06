# coding: utf-8
from schematics.models import Model
from schematics.types import DictType, StringType, ModelType


# dict of string
# dict of model


class A(Model):
    s = StringType()


class B(Model):
    sd = DictType(StringType)
    md = DictType(ModelType(A))


def main():
    b = B()
    b.sd = {
        "e": "ee",
        "f": "ff"
    }
    b.md = {
        "g": A({"s": "ss"})
    }
    print(b.serialize())


if __name__ == '__main__':
    main()
