import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)


def main():
    key = 'foo_set'
    r.sadd(key, 'a')
    r.sadd(key, 1)
    print(r.sismember(key, '1'))
    print(r.scard(key))
    print(r.smembers(key))


if __name__ == '__main__':
    main()
