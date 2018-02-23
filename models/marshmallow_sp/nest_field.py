from marshmallow import Schema, fields


class ButtonSchema(Schema):
    name = fields.Str()


class MenuSchema(Schema):
    buttons = fields.Nested(ButtonSchema(many=True))


def main():
    result = MenuSchema().load({
        'buttons': [
            {
                'name': 'foo'
            },
            {
                'name': 'bar'
            }
        ]
    })
    print(result)


if __name__ == '__main__':
    main()
