from peewee import Model, CharField, IntegerField, IntegrityError

from packages.peewee_sp.mysql_db import db


class BaseModel(Model):
    class Meta:
        database = db


class TranFoo(BaseModel):
    foo = IntegerField(unique=True)


class TranBar(BaseModel):
    bar = IntegerField(unique=True)


def create_tables():
    db.create_tables([TranFoo, TranBar])


@db.atomic()
def create_foo_and_bar():
    TranFoo.create(foo=2)
    TranBar.create(bar=10)


def main():
    # create_tables()
    # TranBar.create(bar=10)
    try:
        create_foo_and_bar()
    except IntegrityError as e:
        print(e)
    print(TranFoo.select().where(TranFoo.foo==2).count())


if __name__ == '__main__':
    main()
