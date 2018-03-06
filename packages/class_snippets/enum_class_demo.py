# coding: utf-8


class MyType(object):
    '''我的类别
    x: x 类型
    y: y 类型
    '''
    x = 1
    y = 2

    type_text_map = {
        x: "x_type",
        y: "y_type"
    }

    text_type_map = {
        "x_type": x,
        "y_type": y
    }

    @classmethod
    def get_text(cls, type_):
        return cls.type_text_map[type_]

    @classmethod
    def get_type(cls, text):
        return cls.text_type_map[text]


def main():
    x = 'x_type'
    print(MyType.get_type(x))
    print(MyType.get_text(MyType.x))


if __name__ == '__main__':
    main()
