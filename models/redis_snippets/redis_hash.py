# coding: utf-8
import redis

hash_key = 'my_hash'
r = redis.StrictRedis(host='localhost', port=6379, db=0)


def set_data():
    r.hset(hash_key, 'foo', 'bar')
    r.hset(hash_key, 'n', 100)


def get_data():
    print('foo: {}'.format(r.hget(hash_key, 'foo')))
    print('bar: {}'.format(r.hget(hash_key, 'bar')))
    print('n: {}'.format(r.hget(hash_key, 'n')))
    print('all: {}'.format(r.hgetall(hash_key)))


def main():
    set_data()
    get_data()
    r.delete(hash_key)

if __name__ == '__main__':
    main()
