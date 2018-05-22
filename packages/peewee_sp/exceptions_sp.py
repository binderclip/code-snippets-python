from peewee import *
from packages.peewee_sp.mysql_db import db


class BaseModel(Model):
    class Meta:
        database = db


class EModel(BaseModel):
    my_char = CharField(max_length=10)


def create_table():
    db.create_tables([EModel])


def drop_table():
    db.create_tables([EModel])


def does_not_exist():
    EModel.get_by_id(11111)  # DoesNotExist


def data_error():
    EModel.create(my_char='a' * 11)  # peewee.DataError: (1406, "Data too long for column 'my_char' at row 1")


def main():
    # create_table()
    # does_not_exist()
    data_error()
    # drop_table()


if __name__ == '__main__':
    main()
