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
    random.seed(int(time.time()))
    max_i = 0xffffffffffffffffffff
    print(max_i)

    db.create_tables([Mass])

    # 20k rows / min, really slow
    # 20000k -> 16.67h
    # for i in range(start, stop):
    #     s = '{:020x}'.format(random.randint(0, max_i))
    #     Mass.insert(id=i, random_str=s).execute()
    #     sys.stdout.write(f'\r{i}')

    # 50k rows/min, slow
    # 20m -> 6.67h
    # for items in chunks(range(start, stop), 100):
    #     with db.atomic():
    #         for i in items:
    #             s = '{:020x}'.format(random.randint(0, max_i))
    #             Mass.insert(id=i, random_str=s).execute()
    #             sys.stdout.write(f'\r{i}')

    # 656k rows/min, fast
    # 20m -> 30m
    # insert_chunks = 100

    # 1.1m rows/min, fast
    # 20m -> 18m
    # real: 900k -> 34s
    # real: 9m -> 6m25s
    insert_chunks = 1000

    # 1.3m rows/min, fast
    # 20m -> 16m
    # insert_chunks = 10000

    for items in chunks(range(start, stop), insert_chunks):
        fields = [Mass.id, Mass.random_str]
        data = [(i, '{:020x}'.format(random.randint(0, max_i))) for i in items]
        Mass.insert_many(data, fields).execute()
        sys.stdout.write(f'\r{items[-1]}')

    print('\n')


if __name__ == '__main__':
    fire.Fire(main)


# http://docs.peewee-orm.com/en/latest/peewee/querying.html#bulk-inserts
