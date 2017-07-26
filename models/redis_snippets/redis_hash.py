# coding: utf-8
import redis

hash_key = 'my_hash'


def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.hset(hash_key, 'hello', 'world')
    print('Hello, {}!'.format(r.hget(hash_key, 'hello')))
    r.delete(hash_key)

if __name__ == '__main__':
    main()
