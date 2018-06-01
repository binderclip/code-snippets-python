from peewee import *
from playhouse.shortcuts import model_to_dict

from packages.peewee_sp.mysql_db import db


class UnsignedBigIntegerField(BigIntegerField):
    field_type = 'bigint unsigned'


class UnsignedIntegerField(IntegerField):
    field_type = 'int unsigned'


class BaseModel(Model):
    class Meta:
        database = db


class CustBoss(BaseModel):
    my_unbiginteger = UnsignedBigIntegerField()
    my_biginteger = BigIntegerField()
    my_uninteger = UnsignedIntegerField()
    my_integer = IntegerField()


def main():
    db.connect()
    db.create_tables([CustBoss])
    n = 2 ** 63
    n2 = 2 ** 31
    CustBoss.create(my_unbiginteger=n, my_biginteger=n - 1, my_uninteger=n2, my_integer=n2 - 1)
    # CustBoss.create(my_unbiginteger=n, my_biginteger=n, my_uninteger=n2, my_integer=n2 - 1)     # peewee.DataError: (1264, "Out of range value for column 'my_biginteger' at row 1")
    # CustBoss.create(my_unbiginteger=n, my_biginteger=n - 1, my_uninteger=n2, my_integer=n2)  peewee.DataError: (1264, "Out of range value for column 'my_integer' at row 1")
    query = CustBoss.select()
    for b in query:
        print(model_to_dict(b))


if __name__ == '__main__':
    main()
