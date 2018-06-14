from peewee import *
from packages.peewee_sp.mysql_db import db


class BaseModel(Model):
    class Meta:
        database = db


class OrderItem(BaseModel):
    order_num = IntegerField()
    order_item = IntegerField()



def create_db():
    db.create_tables([OrderItem])


def insert_values():
    print('=== insert_values ===')
    data = [
        (1, 100),
        (1, 200),
        (2, 100),
        (2, 200),
    ]
    fields = [OrderItem.order_num, OrderItem.order_item]
    OrderItem.insert_many(data, fields=fields).execute()


def get_values():
    print('=== get_values ===')
    print('order_num > order_item')
    for item in OrderItem.select().order_by(OrderItem.order_num, OrderItem.order_item):
        print(f'num: {item.order_num}, item: {item.order_item}')
    print('order_item > order_num')
    for item in OrderItem.select().order_by(OrderItem.order_item, OrderItem.order_num):
        print(f'num: {item.order_num}, item: {item.order_item}')


def main():
    create_db()
    # insert_values()
    get_values()


if __name__ == '__main__':
    main()
