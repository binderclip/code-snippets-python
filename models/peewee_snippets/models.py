# coding: utf-8
import datetime
from peewee import *

from .mysql_db import db


class Person(Model):

    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db
        table_name = 'person'


class Ppp(Model):
    name = CharField()
    create_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
