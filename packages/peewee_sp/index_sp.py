from peewee import *
from packages.peewee_sp.mysql_db import db


class BaseModel(Model):
    class Meta:
        database = db


class BigIndex(BaseModel):
    my_integer = IntegerField(index=True)
    my_char = CharField(unique=True)

    class Meta:
        indexes = (
            (('my_integer', 'my_char', ), False),
        )


def main():
    db.connect()
    db.create_tables([BigIndex])


if __name__ == '__main__':
    main()
