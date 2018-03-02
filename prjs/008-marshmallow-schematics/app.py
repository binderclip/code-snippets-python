from schemas import FooSchema
from dtos import FooDTO
from daos import FooDAO


def main():
    dao = FooDAO('baz_dao')
    d = {"bar": "baz_d"}

    dto = FooDTO(d)
    print(dto.serialize())

    dto, errors = FooSchema().dump(dao)
    print(dto.serialize())

    # print(FooSchema().load(dao))
    # print(FooSchema().load(d))
    # print(FooSchema().dump(dao))


if __name__ == '__main__':
    main()
