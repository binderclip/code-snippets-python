# coding: utf-8
from peewee import Model, CharField, DateField, BooleanField

from playhouse.db_url import connect


MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_DB_NAME = "test_db"
MYSQL_DB_URL = "mysql://{user}:{password}@{host}:{port}/{db_name}".format(
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    db_name=MYSQL_DB_NAME,
)


db = connect(MYSQL_DB_URL)


class Person(Model):
    
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

