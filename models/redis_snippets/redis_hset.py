# coding: utf-8
import redis

hash_key = 'my_hash'
hash_key2 = 'my_hash2'
r = redis.StrictRedis(host='localhost', port=6379, db=0)


def set_data():
    print('===== set_data =====')
    print('hset: {}'.format(r.hset(hash_key, 'foo', 'bar')))    # 返回值是是否新建
    print('hset: {}'.format(r.hset(hash_key, 'n', 100)))
    r.hset(hash_key, 'a', 'aa')
    r.hset(hash_key, 'b', 'bb')


def incr_data():
    print('===== incr_data =====')
    print('hincrby: {}'.format(r.hincrby(hash_key, 'n', 1)))    # 返回值是增加后的值


def get_data():
    print('===== get_data =====')
    print('foo: {}'.format(r.hget(hash_key, 'foo')))
    print('bar: {}'.format(r.hget(hash_key, 'bar')))
    print('n: {}'.format(r.hget(hash_key, 'n')))
    print('all: {}'.format(r.hgetall(hash_key)))
    print('all keys: {}'.format(r.hgetall(hash_key).keys()))


def rem_data():
    print('===== rem_data =====')
    r.hdel(hash_key, 'a')


def set_hash_to_str():
    print('===== set_hash_to_str =====')
    r.set(hash_key2, 'bar')
    print('hash_key2: {}'.format(r.get(hash_key2)))
    r.delete(hash_key2)     # 不删除的话就会 WRONGTYPE Operation
    r.hset(hash_key2, 'foo', 'bar')
    print('hash_key2: {}'.format(r.hgetall(hash_key2)))


def main():
    set_data()
    incr_data()
    get_data()
    rem_data()
    get_data()
    set_hash_to_str()
    r.delete(hash_key)

if __name__ == '__main__':
    main()
