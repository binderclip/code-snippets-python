import datetime
from peewee import *

db = SqliteDatabase('data.db')


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
