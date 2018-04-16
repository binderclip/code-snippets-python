from pydantic import BaseModel


class MyData:

    def __init__(self, s):
        self.s = s


    def __str__(self):
        return f'<MyData s: {self.s}>'

    @classmethod
    def get_validators(cls):
        yield cls.myvalidator

    @classmethod
    def myvalidator(cls, v):
        return cls(v)


class MyModel(BaseModel):
    md: MyData


def main():
    model = MyModel.parse_obj({
        "md": "hello"
    })
    print(model.md)


if __name__ == '__main__':
    main()
