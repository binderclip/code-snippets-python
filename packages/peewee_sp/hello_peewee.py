# coding: utf-8
import datetime
from peewee import *
from mysql_db import db


class BaseModel(Model):

    class Meta:
        database = db

    def save(self, *args, **kwargs):
        if hasattr(self, 'update_time'):
            self.update_time = datetime.datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)

    @classmethod
    def get(cls, *query, **kwargs):
        try:
            return super(BaseModel, cls).get(*query, **kwargs)
        except DoesNotExist:
            return None


class Person(BaseModel):
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)

    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()


class Pet(BaseModel):
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)

    owner_id = IntegerField()
    name = CharField()
    animal_type = CharField()


def create_db_and_tables():
    print('=== create db and tables ===')
    db.connect()
    db.create_tables([Person, Pet])


def new_user1():
    print('=== new_user1 ===')
    uncle_bob = Person(name='Bob', birthday=datetime.date(1960, 1, 15), is_relative=True)
    uncle_bob.save()


def new_user2():
    print('=== new_user2 ===')
    little_tim = Person(name='Tim', birthday=datetime.date(1999, 3, 15), is_relative=True)
    little_tim.save()


def _print_person(p):
    print("id: {}, name: {}, birthday: {}, is_relative: {}".format(p.id, p.name, p.birthday, p.is_relative))


def get_user():
    print('=== get_user ===')
    for name in ['Bob', 'Tim', 'Nil']:
        p = Person.get(name=name)
        if p:
            _print_person(p)
        else:
            print("person name={} dose not exist".format(name))


def where_user():
    print('=== where_user ===')
    names = ['Bob', 'Tim', 'Nil']
    query = Person.select().where(Person.name in names)
    for p in query:
        _print_person(p)


def new_pet1():
    pass


def new_pet2():
    pass


def main():
    # create_db_and_tables()
    # new_user1()
    # new_user2()
    get_user()
    where_user()


if __name__ == '__main__':
    main()
