from marshmallow import Schema, fields, post_load
from marshmallow_polyfield import PolyField


class Button(object):
    def __init__(self, type, name):
        self.type = type
        self.name = name


class ClickButton(Button):
    def __init__(self, type, name, key):
        super(ClickButton, self).__init__(type, name)
        self.key = key


class ViewButton(Button):
    def __init__(self, type, name, url):
        super(ViewButton, self).__init__(type, name)
        self.url = url


class ButtonSchema(Schema):
    type = fields.Str()
    name = fields.Str()


class ClickButtonSchema(ButtonSchema):
    key = fields.Str()

    @post_load
    def make_object(self, data):
        return ClickButton(
            type=data['type'],
            name=data['name'],
            key=data['key'],
        )


class ViewButtonSchema(ButtonSchema):
    url = fields.Str()

    @post_load
    def make_object(self, data):
        return ViewButton(
            type=data['type'],
            name=data['name'],
            url=data['url'],
        )


# button group


def button_serialization_schema_selector(_, obj):
    type_to_schema = {
        'click': ClickButtonSchema,
        'view': ViewButtonSchema,
    }
    try:
        return type_to_schema[obj.type]()
    except KeyError:
        raise TypeError("Could not detect type. "
                        "Did not have a base or a length. "
                        "Are you sure this is a shape?")


def button_deserialization_schema_selector(data, _):
    type_to_schema = {
        'click': ClickButtonSchema,
        'view': ViewButtonSchema,
    }
    try:
        return type_to_schema[data['type']]()
    except KeyError:
        raise TypeError("Could not detect type. "
                        "Did not have a base or a length. "
                        "Are you sure this is a shape?")


class MenuSchema(Schema):
    buttons = PolyField(
        serialization_schema_selector=button_serialization_schema_selector,
        deserialization_schema_selector=button_deserialization_schema_selector,
        many=True,
    )


def main():
    result = MenuSchema().load({
        'buttons': [
            {
                'name': '点我',
                'type': 'click',
                'key': 'key001',
            },
            {
                'name': '跳转',
                'type': 'view',
                'url': 'http://foo.com',
            }
        ]
    })
    print(result)


if __name__ == '__main__':
    main()
