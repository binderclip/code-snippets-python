# coding: utf-8
import redis
from profilehooks import profile


@profile
def read_from_redis(r, n, d):
    for i in xrange(n):
        d[str(n - 1 - i)] = r.get(str(i))


def main():
    d = {}
    r = redis.StrictRedis(host='localhost', port=6379, db=0)

    read_from_redis(r, 10000, d)


if __name__ == '__main__':
    main()
