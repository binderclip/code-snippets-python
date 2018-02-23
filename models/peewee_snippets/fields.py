from peewee import *
from playhouse.db_url import connect


MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_DB_NAME = "test_db"
MYSQL_DB_URL = "mysql://{user}:{password}@{host}:{port}/{db_name}?charset=utf8mb4".format(
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    db_name=MYSQL_DB_NAME,
)

db = connect(MYSQL_DB_URL)


# db = SqliteDatabase('fields.db')


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
    my_fixedchar = FixedCharField()
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
