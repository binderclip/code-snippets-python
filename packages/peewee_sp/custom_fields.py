import time

import datetime

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
    my_uninteger2 = IntegerField(null=True, constraints=[SQL('UNSIGNED')])      # error when null=False, so this may be not a good way
    my_integer = IntegerField()
    my_default_integer = IntegerField(constraints=[SQL('DEFAULT 100')])
    my_default_datetime = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    my_default_update_datetime = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')])


def main():
    db.connect()
    db.create_tables([CustBoss])
    n = 2 ** 63
    n2 = 2 ** 31
    cust_boss = CustBoss.create(my_unbiginteger=n, my_biginteger=n - 1, my_uninteger=n2, my_uninteger2=n2, my_integer=n2 - 1)
    time.sleep(1)
    cust_boss.my_integer -= 1
    cust_boss.save()
    # CustBoss.create(my_unbiginteger=n, my_biginteger=n, my_uninteger=n2, my_uninteger2=n2, my_integer=n2 - 1)     # peewee.DataError: (1264, "Out of range value for column 'my_biginteger' at row 1")
    # CustBoss.create(my_unbiginteger=n, my_biginteger=n - 1, my_uninteger=n2, my_uninteger2=n2, my_integer=n2)  peewee.DataError: (1264, "Out of range value for column 'my_integer' at row 1")
    query = CustBoss.select()
    for b in query:
        print(model_to_dict(b))


if __name__ == '__main__':
    main()

# http://peewee.readthedocs.io/en/latest/peewee/models.html#creating-a-custom-field
# http://docs.peewee-orm.com/en/latest/peewee/models.html#default-field-values
