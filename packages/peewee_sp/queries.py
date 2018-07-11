from peewee import *
from packages.peewee_sp.mysql_db import db


class BaseModel(Model):

    class Meta:
        database = db


class Foo(BaseModel):
    name = CharField()
    type = SmallIntegerField()

    @property
    def upper_name(self):
        return self.name.upper()

    def __str__(self):
        return f'Foo(id: {self.id}, name: {self.name}, type: {self.type})'

    def __repr__(self):
        return self.__str__()


class FooType(object):
    TA = 1
    TB = 2
    TC = 3


def create_tables():
    print('=== create_tables ===')
    db.connect()
    db.create_tables([Foo])


def insert_row():
    print('=== insert_row ===')
    query = Foo.insert({
        Foo.name: 'n1',
        Foo.type: FooType.TA,
    })
    r = query.execute()
    print(r)    # 插入的这条数据的 id
    Foo.insert(name='n2', type=FooType.TA).execute()
    Foo.insert(name='n3', type=FooType.TB).execute()
    Foo.insert(name='n4', type=FooType.TC).execute()


def insert_many_rows():
    print('=== insert_many_rows ===')
    data_source = [
        {
            Foo.name: 'n10',
            Foo.type: FooType.TA,
        },
        {
            Foo.name: 'n11',
            Foo.type: FooType.TB,
        }
    ]
    r = Foo.insert_many(data_source).execute()
    print(r)    # 插入的第一条数据的 id

    data = [('n10', FooType.TB), ('n10', FooType.TC)]
    fields = [Foo.name, Foo.type]
    Foo.insert_many(data, fields=fields).execute()


def insert_or_update():
    print("=== insert_or_update ===")
    # http://docs.peewee-orm.com/en/latest/peewee/api.html#Insert.on_conflict
    # Foo.insert(id=100, name='n2', type=FooType.TA).execute()
    r = Foo.insert(id=101, name='n2', type=FooType.TA).on_conflict(update={
        Foo.name: 'n2_',
        Foo.type: FooType.TA,
    }).execute()    # 如果有插入或者有更新的话会返回那一行的 id，否则返回 0
    print(r)
    print(Foo.get_by_id(101))


def insert_or_update2():
    print("=== insert_or_update2 ===")
    insert_new = False
    try:
        r = Foo.insert(id=100, name='n2', type=FooType.TA).execute()    # 返回插入行的 id
        insert_new = True
    except IntegrityError:
        r = Foo.update(name='n2').where(Foo.id == 100).execute()    # 返回更新的行数
    print(f'r: {r}, insert_new: {insert_new}')
    print(Foo.get_by_id(100))


def create_row():
    print('=== create_row ===')
    foo = Foo.create(name='n5', type=FooType.TB)
    print(foo)
    foo = Foo.create(name='n6', type=FooType.TA)
    print(foo)


def get_or_create():
    print('=== get_or_create ===')
    foo, created = Foo.get_or_create(
        id=7,
        defaults={'name': 'n7', 'type': FooType.TA})
    print(foo, created)


def save_row():
    print('=== save_row ===')
    foo = Foo(name='n5', type=FooType.TB)
    print(foo)
    foo2 = foo.save()
    print(foo)
    print(foo2)


def update_some():
    print('=== update_some ===')
    # id < 3, type = type + 1
    r = Foo.update({Foo.type: Foo.type + 1}).where(Foo.id < 3).execute()
    # id < 3, type = 1
    r = Foo.update(type=FooType.TB).where(Foo.id < 3).execute()
    print(r)    # 返回值为修改的行数，没有发生实际修改的不计数


def get_one():
    print('=== get_one ===')
    foo1 = Foo.get()
    print(foo1)
    foo2 = Foo.get(id=2)
    print(foo2)
    foo100x = Foo.get(100)    # ERROR!!!
    print(foo100x)
    foo100 = Foo.get_by_id(100)
    print(foo100)
    foo3x = Foo.get(id=3, name='x')
    print(foo3x)


def get_all():
    print('=== get_all ===')
    query = Foo.select()
    print(query)
    print(list(query))
    for foo in query:
        print(foo)
    print(len(query))


def get_specific_columns():
    print('=== get_specific_columns ===')
    query = Foo.select(Foo.id, Foo.name)
    # TODO: query 里的迭代是怎样执行的
    for foo_data in query:
        print(f'id: {foo_data.id}, name: {foo_data.name}')


def get_specific_rows():
    print('=== get_specific_rows ===')
    print('Foo.id < 3')
    query = Foo.select().where(Foo.id < 3)
    for foo in query:
        print(foo)
    print('not Foo.id < 3')
    query = Foo.select().where(~(Foo.id < 3))
    for foo in query:
        print(foo)
    print('Foo.type == FooType.TA')
    query = Foo.select().where(Foo.type == FooType.TA)
    for foo in query:
        print(foo)
    print('Foo.type == FooType.TA && Foo.id > 1')
    query = Foo.select().where((Foo.type == FooType.TA) & (Foo.id > 1))
    for foo in query:
        print(foo)
    print('Foo.type == FooType.TA || Foo.id > 1')
    query = Foo.select().where((Foo.type == FooType.TA) | (Foo.id > 1))
    for foo in query:
        print(foo)
    print('Foo.type in (FooType.TB, FooType.TC)')
    query = Foo.select().where(Foo.type.in_([FooType.TB, FooType.TC]))
    for foo in query:
        print(foo)
    print('Foo.type not in (FooType.TB, FooType.TC)')
    query = Foo.select().where(Foo.type.not_in([FooType.TB, FooType.TC]))
    for foo in query:
        print(foo)


def delete_rows():
    print('=== delete_rows ===')
    print(Foo.select().count())
    foo = Foo.get_by_id(1)
    foo.delete_instance()

    print(Foo.delete_by_id(4))     # 删除不存在的内容不会报错，但会返回影响的行数

    Foo.delete().where(Foo.type == FooType.TB).execute()
    print(Foo.select().count())


def get_ordered_rows():
    print('=== get_ordered_rows ===')
    query = Foo.select().order_by(Foo.id.desc())
    for foo in query:
        print(foo)


def get_count():
    print('=== get_count ===')
    query = Foo.select().where(Foo.type == FooType.TA).count()
    print(query)


def get_with_limit_offset():
    print('=== get_with_limit_offset ===')
    print('offset 1 limit 2')
    query = Foo.select().order_by(Foo.id).offset(1).limit(2)
    for foo in query:
        print(foo)
    print('offset 2 limit 2')
    query = Foo.select().order_by(Foo.id).offset(2).limit(2)
    for foo in query:
        print(foo)


def get_with_paginate():
    print('=== get_with_paginate ===')
    print('page 1 2')
    query = Foo.select().order_by(Foo.id).paginate(1, 2)
    for foo in query:
        print(foo)
    print('page 2 2')
    query = Foo.select().order_by(Foo.id).paginate(2, 2)
    for foo in query:
        print(foo)


def sql_of_query():
    print('=== sql_of_query ===')
    query = Foo.select().order_by(Foo.id).offset(2).limit(2)
    print(query.sql())


def main():
    # create_tables()
    # insert_row()
    # insert_many_rows()
    # # create_row()
    # insert_or_update()
    # insert_or_update2()
    # try:
    #     get_one()
    # except DoesNotExist as e:
    #     print(e)
    # get_all()
    # get_specific_columns()
    get_specific_rows()
    # get_ordered_rows()
    # get_count()
    # get_with_limit_offset()
    # get_with_paginate()
    # get_or_create()
    # save_row()
    # update_some()
    # delete_rows()
    # sql_of_query()


if __name__ == '__main__':
    main()

# http://docs.peewee-orm.com/en/latest/peewee/querying.html
# http://docs.peewee-orm.com/en/latest/peewee/query_operators.html
