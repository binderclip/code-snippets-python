from dataclasses import dataclass, asdict


@dataclass
class SimpleDataObject(object):
    field_x: str


@dataclass
class SimpleDataObjectA(SimpleDataObject):
    field_a: int


@dataclass
class SimpleDataObjectB(SimpleDataObject):
    field_b: str


@dataclass
class DataObject(object):
    field_c: int
    s_obj: SimpleDataObject


def main():
    d2 = {'field_c': 100, 's_obj': SimpleDataObject(**{'field_a': 1, 'field_b': 'aaa'})}
    d2 = {'field_c': 100, 's_obj': {'field_a': 1, 'field_b': 'aaa'}}
    obj2 = DataObject(**d2)
    print(obj2)


if __name__ == '__main__':
    main()
