# coding: utf-8
import redis
import time


r = redis.StrictRedis(host='localhost', port=6379, db=0)


def setex():
    print('===== setex =====')
    r.setex('Hello', 1, 'World')
    print('Hello, {}!'.format(r.get('Hello')))
    time.sleep(0.5)
    print('Hello, {}!'.format(r.get('Hello')))
    time.sleep(0.5)
    print('Hello, {}!'.format(r.get('Hello')))


def hsetex():
    print('===== hsetex =====')
    hash_key = 'my_hash'
    r.hset(hash_key, 'Hello', 'World')
    r.expire(hash_key, 1)   # no hsetex，也不能单个的设置 ex
    print('Hello, {}!'.format(r.hget(hash_key, 'Hello')))
    time.sleep(0.5)
    print('Hello, {}!'.format(r.hget(hash_key, 'Hello')))
    time.sleep(0.5)
    print('Hello, {}!'.format(r.hget(hash_key, 'Hello')))
    r.delete(hash_key)


def main():
    setex()
    hsetex()


if __name__ == '__main__':
    main()
