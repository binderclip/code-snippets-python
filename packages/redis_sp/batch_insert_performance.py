# coding: utf-8
import time
import redis
from profilehooks import profile


@profile
def insert_to_redis(r, n, start):
    for i in xrange(n):
        r.set(str(i) + str(start), 'x')


def main():
    start = int(time.time())
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    insert_to_redis(r, 10000, start)


if __name__ == '__main__':
    main()
