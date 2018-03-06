# coding: utf-8
from schematics.models import Model
from schematics.types import StringType, PolyModelType


# 普通的 model
def models():
    print("=== models ===")

    class TextMsg(Model):
        type_ = StringType()
        text = StringType()

    class ImageMsg(Model):
        type_ = StringType()
        image = StringType()

    class MyModel(Model):
        msg = PolyModelType([TextMsg, ImageMsg])

    m1 = MyModel()
    m1.msg = TextMsg({"type_": "text", "text": "ttt"})
    m2 = MyModel()
    m2.msg = ImageMsg({"type_": "img", "image": "iii"})
    print(m1.serialize())
    print(m2.serialize())


# 使用了继承的
def inherit_models():
    print("=== inherit_models ===")

    class Msg(Model):
        type_ = StringType()

    class TextMsg(Msg):
        text = StringType()

    class ImageMsg(Msg):
        image = StringType()

    class MyModel(Model):
        msg = PolyModelType(Msg)

    m1 = MyModel()
    m1.msg = TextMsg({"type_": "text", "text": "ttt"})
    m2 = MyModel()
    m2.msg = ImageMsg({"type_": "img", "image": "iii"})
    print(m1.serialize())
    print(m2.serialize())
    # m3 = MyModel({'msg': {'type_': 'img', 'image': 'iii'}})     # schematics.exceptions.DataError: {"msg": {"image": "Rogue field"}}


# 自动区分的
def claim_models():
    print("=== claim_models ===")

    class Msg(Model):
        type_ = StringType()

    class TextMsg(Msg):
        text = StringType()

    class ImageMsg(Msg):
        image = StringType()

    def claim_func(field, data):
        if data['type_'] == 'text':
            return TextMsg
        elif data['type_'] == 'image':
            return ImageMsg
        else:
            return None

    class MyModel(Model):
        msg = PolyModelType(Msg, claim_function=claim_func)

    m3 = MyModel({'msg': {'type_': 'text', 'text': 'ttt'}})     # schematics.exceptions.DataError: {"msg": {"image": "Rogue field"}}
    print(m3.serialize())
    m4 = MyModel({'msg': {'type_': 'image', 'image': 'iii'}})     # schematics.exceptions.DataError: {"msg": {"image": "Rogue field"}}
    print(m4.serialize())


def main():
    models()
    inherit_models()
    claim_models()


if __name__ == '__main__':
    main()

# https://github.com/schematics/schematics/blob/master/tests/test_polymodeltype.py
