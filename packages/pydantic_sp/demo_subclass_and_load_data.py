from pydantic import BaseModel


class Foo(BaseModel):
    foo: str


class Bar(Foo):
    bar: str


class FooView(BaseModel):
    foo_uc: str  # uppercase

    @classmethod
    def trans_data(cls, data: dict) -> dict:
        data = data.copy()
        data['foo_uc'] = data['foo'].upper()
        return data


class BarView(FooView):
    bar_lc: str

    @classmethod
    def trans_data(cls, data: dict) -> dict:
        data = super().trans_data(data)
        data['bar_lc'] = data['bar'].lower()
        return data


def main():
    bar = Bar.parse_obj({'foo': 'f', 'bar': 'B'})
    print(bar)
    bar_view = BarView.parse_obj(BarView.trans_data(bar.dict()))
    print(bar_view)


if __name__ == '__main__':
    main()

