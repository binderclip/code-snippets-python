from dataclasses import dataclass, asdict


@dataclass
class SimpleDataObject(object):
    field_a: int
    field_b: str


@classmethod
class DataObject(object):
    field_c: int
    s_obj: SimpleDataObject


def main():
    obj = SimpleDataObject(1, 'aaa')
    print(obj)
    print(asdict(obj))

    obj2 = SimpleDataObject(100, obj)
    print(obj2)
    print(asdict(obj2))

    d = {'field_a': 1, 'field_b': 'aaa'}
    obj = SimpleDataObject(field_a=1, field_b='aaa')
    print(obj)
    obj = SimpleDataObject(**d)
    print(obj)
    print(type(obj))

    # d2 = {'field_a': 100, 'field_b': {'field_a': 1, 'field_b': 'aaa'}}
    # obj2 = DataObject()
    # obj2 = DataObject(**d2)
    # print(obj2)


if __name__ == '__main__':
    main()
