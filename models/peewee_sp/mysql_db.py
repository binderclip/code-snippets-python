from peewee import __exception_wrapper__
from peewee import MySQLDatabase
from peewee import OperationalError
# from playhouse.db_url import connect


MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_DB_NAME = "test_db"
MYSQL_CHARSET = 'utf8mb4'
# MYSQL_DB_URL = "mysql://{user}:{password}@{host}:{port}/{db_name}?charset=utf8mb4".format(
#     user=MYSQL_USER,
#     password=MYSQL_PASSWORD,
#     host=MYSQL_HOST,
#     port=MYSQL_PORT,
#     db_name=MYSQL_DB_NAME,
# )
# db = connect(MYSQL_DB_URL)


class MySQLRTDatabase(MySQLDatabase):

    def execute_sql(self, sql, params=None, commit=True):
        try:
            cursor = super(MySQLRTDatabase, self).execute_sql(
                sql, params, commit)
        except OperationalError:
            if not self.is_closed():
                self.close()
            with __exception_wrapper__:
                cursor = self.cursor()
                cursor.execute(sql, params or ())
                if commit and not self.in_transaction():
                    self.commit()
        return cursor


db = MySQLRTDatabase(
        MYSQL_DB_NAME,
        user=MYSQL_USER,
        host=MYSQL_HOST,
        password=MYSQL_PASSWORD,
        charset=MYSQL_CHARSET,
    )
