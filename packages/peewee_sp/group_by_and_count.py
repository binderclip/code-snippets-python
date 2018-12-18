from peewee import *

from packages.peewee_sp.mysql_db import db


class BaseModel(Model):
    class Meta:
        database = db


class Comment(BaseModel):
    parent_id = IntegerField()


def create():
    db.connect()
    db.create_tables([Comment])
    Comment.create(parent_id=1)
    Comment.create(parent_id=1)
    Comment.create(parent_id=2)


def main():
    # create()
    query = (Comment.select(Comment.parent_id, fn.COUNT(Comment.id).alias('ct'))
             .group_by(Comment.parent_id))
    for obj in query:
        print(obj.parent_id, obj.ct)


if __name__ == '__main__':
    main()


# https://stackoverflow.com/questions/45760563/returning-a-count-of-grouped-items-in-peewee-orm
