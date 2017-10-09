# coding: utf-8
import datetime
from schematics.models import Model
from schematics.types import StringType, IntType, DateTimeType, ModelType


class HelloSchematics(Model):

    foo = StringType()


class MyDefault(Model):

    s1 = StringType()
    s2 = StringType(default="")
    s3 = StringType(default="x")

    i1 = IntType()
    i2 = IntType(default=0)
    i3 = IntType(default=1)


class MyFields(Model):

    s = StringType(default="s")
    d = DateTimeType(default=datetime.datetime.now)


class MyValidate(Model):
    city = StringType(required=True)
    taken_at = DateTimeType(default=datetime.datetime.now)


class ModelDetail(Model):
    detail1 = StringType()
    detail2 = StringType()


class MyModel(Model):
    s = StringType()
    detail = ModelType(ModelDetail)


def hello():
    print("=== hello ===")
    hello_schematics = HelloSchematics({'foo': 'bar'})
    print(hello_schematics.to_native())
    hello_schematics2 = HelloSchematics()
    print(hello_schematics2.to_native())
    hello_schematics2.foo = 'bar2'
    print(hello_schematics2.to_native())
    hello_schematics2.foo = 'bar3'
    print(hello_schematics2.to_native())
    hello_schematics2.foo2 = 'bar4'
    print(hello_schematics2.to_native())


def default_value():
    print("=== default_value ===")
    my_default = MyDefault()
    print(my_default.to_native())


def conversion():
    print("=== conversion ===")
    my_fields = MyFields()
    print("serialize(): {}".format(my_fields.serialize()))
    print("to_native(): {}".format(my_fields.to_native()))
    print("to_primitive(): {}".format(my_fields.to_primitive()))


def conversion2():
    print("=== conversion2 ===")
    dt_t = DateTimeType()
    dt = dt_t.to_native('2013-08-31T02:21:21.486072')
    print("type: {}, value: {}".format(type(dt), dt))
    print("type: {}, value: {}".format(type(dt_t.to_primitive(dt)), dt_t.to_primitive(dt)))


def validate():
    print("=== validate ===")
    my_validate = MyValidate()
    # my_validate.validate()  # schematics.exceptions.DataError: {"city": ["This field is required."]}
    my_validate.city = "BEIJING"
    my_validate.validate()
    my_validate.taken_at = 'x'
    # my_validate.validate()
    # schematics.exceptions.DataError: {"taken_at": ["Could not parse x. Should be ISO 8601 or timestamp."]}
    my_validate.taken_at = datetime.datetime.now()
    my_validate.validate()
    print('validate pass')


def validate_2():
    print("=== validate_2 ===")
    st = StringType(max_length=10)
    st.to_native('this is longer than 10')
    # st.validate('this is longer than 10')   # schematics.exceptions.ValidationError: ["String value is too long."]


def model_in_model():
    print("=== model_in_model ===")
    my_model = MyModel()
    my_model.s = 'sss'
    print(my_model.to_native())
    print(my_model.to_primitive())
    my_model.detail = {}
    print(my_model.to_native())
    print(my_model.to_primitive())
    my_model.detail = {'detail1': 'd1'}
    print(my_model.to_native())
    print(my_model.to_primitive())
    my_model.detail = ModelDetail({'detail2': 'd2'})
    print(my_model.to_native())
    print(my_model.to_primitive())


def main():
    hello()
    default_value()
    conversion()
    conversion2()
    validate()
    validate_2()
    model_in_model()


if __name__ == '__main__':
    main()
