import redis
import time


r = redis.StrictRedis(host='localhost', port=6379, db=0)


def setex():
    print('=== setex ===')
    key = 'Hello'
    r.setex(key, 1, 'World')
    print('Hello, {}!'.format(r.get(key)))
    time.sleep(0.5)
    print('Hello, {}!'.format(r.get(key)))
    time.sleep(0.5)
    print('Hello, {}!'.format(r.get(key)))


def set_ex():
    print('=== set ex ===')
    key = 'Hello'
    r.set(key, 'World', ex=1)
    time.sleep(0.5)
    print('Hello, {}!'.format(r.get(key)))
    time.sleep(0.5)
    print('Hello, {}!'.format(r.get(key)))


def hsetex():
    print('=== hsetex ===')
    hash_key = 'my_hash'
    key = 'Hello'
    r.hset(hash_key, key, 'World')
    r.expire(hash_key, 1)   # no hsetex，也不能单个的设置 ex
    print('Hello, {}!'.format(r.hget(hash_key, key)))
    time.sleep(0.5)
    print('Hello, {}!'.format(r.hget(hash_key, key)))
    time.sleep(0.5)
    print('Hello, {}!'.format(r.hget(hash_key, key)))
    r.delete(hash_key)


def ttl():
    print('===== ttl =====')
    key = 'Hello'
    r.setex(key, 1, 'World')
    time.sleep(0.5)
    print('ttl {}'.format(r.ttl(key)))
    time.sleep(0.5)
    print('ttl {}'.format(r.ttl(key)))
    print('value: {}'.format(r.get(key)))


def main():
    # setex()
    # set_ex()
    hsetex()
    # ttl()


if __name__ == '__main__':
    main()
