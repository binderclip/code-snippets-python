from peewee import *
from .mysql_db import db


class BaseModel(Model):
    class Meta:
        database = db


class BigBoss(BaseModel):
    my_integer = IntegerField()
    my_biginteger = BigIntegerField()
    my_smallinteger = SmallIntegerField()
    my_auto = AutoField()
    my_float = FloatField()
    my_double = DoubleField()
    my_decimal = DecimalField()
    my_char = CharField()
    my_fixedchar = FixedCharField()     # max_length=
    my_text = TextField()
    my_blob = BlobField()
    my_bit = BitField()
    my_big_bit = BigBitField()
    my_uuid = UUIDField()
    my_datetime = DateTimeField()
    my_date = DateField()
    my_time = TimeField()
    my_timestamp = TimestampField()
    my_ip = IPField()
    my_boolean = BooleanField()
    # my_bare = BareField()
    # my_foreignkey = ForeignKeyField()


def main():
    db.connect()
    db.create_tables([BigBoss])


if __name__ == '__main__':
    main()
