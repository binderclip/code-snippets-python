from playhouse.shortcuts import model_to_dict, dict_to_model, update_model_from_dict

from queries import Foo


def main():
    foo = Foo.get(id=1)
    print(foo)
    print(model_to_dict(foo))
    print(model_to_dict(foo, exclude=[Foo.type]))

    d = {
        'id': 1,
        'name': 'n1',
        'type': 1,
    }
    foo = dict_to_model(Foo, d)
    print(foo)

    d['type'] = 2
    update_model_from_dict(foo, d)
    print(foo)

    d['id'] = 2
    update_model_from_dict(foo, d)      # id 同样会改掉
    print(foo)


if __name__ == '__main__':
    main()
