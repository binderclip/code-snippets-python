# coding: utf-8
import time
import pymysql.cursors
from profilehooks import profile


@profile
def insert_to_mysql(connection, n, start):
    try:
        with connection.cursor() as cursor:
            for i in xrange(n):
                sql = "INSERT INTO `ab3` (`a`, `b`) VALUES (%s, %s)"
                cursor.execute(sql, (str(i) + str(start), str(start) + str(i)))
        connection.commit()

    finally:
        connection.close()



def main():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',
                                 db='testdb',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    start = int(time.time())
    insert_to_mysql(connection, 10000, start)


if __name__ == '__main__':
    main()
