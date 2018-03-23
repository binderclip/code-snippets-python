import random
import sys
import time

import fire
from peewee import FixedCharField, Model
from playhouse.db_url import connect

MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_DB_NAME = "test_db"
MYSQL_CHARSET = 'utf8mb4'
MYSQL_DB_URL = "mysql://{user}:{password}@{host}:{port}/{db_name}?charset=utf8mb4".format(
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    port=MYSQL_PORT,
    db_name=MYSQL_DB_NAME,
)
db = connect(MYSQL_DB_URL)


def chunks(l, n):
    """ Yield successive n-sized chunks from l. """
    for i in range(0, len(l), n):
        yield l[i:i+n]


class Mass(Model):

    random_str = FixedCharField(max_length=64)

    class Meta:
        database = db


def main(start, stop):
    query = Mass.select().where(start <= Mass.id <= stop)
    # without execute
    print(query)
    s = input('print? ')
    if not s:
        return
    # execute and get all data when fetch data from query for the first time
    for i, item in enumerate(query):
        if i > 1000:
            return
        print(item)


if __name__ == '__main__':
    fire.Fire(main)


# http://docs.peewee-orm.com/en/latest/peewee/querying.html#bulk-inserts
