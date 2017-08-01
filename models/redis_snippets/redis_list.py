# coding: utf-8
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
list_key = 'my_list'


def push():
    print('===== push =====')
    r.rpush(list_key, 'd')
    r.rpush(list_key, 'e', 'f')
    r.lpush(list_key, 'c')
    r.lpush(list_key, 'b', 'a')
    print(r.lrange(list_key, 0, -1))


def pop():
    pass


def main():
    push()
    r.delete(list_key)


if __name__ == '__main__':
    main()
