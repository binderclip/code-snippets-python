# coding: utf-8
import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
list_key = 'my_list'
list_key2 = 'my_list2'
list_key3 = 'my_list3'


def push():
    print('===== push =====')
    r.rpush(list_key, 'd')
    r.rpush(list_key, 'e', 'f')
    r.lpush(list_key, 'c')
    r.lpush(list_key, 'b', 'a')
    print(r.lrange(list_key, 0, -1))
    r.lpush(list_key2, 'a')


def pop():
    print('===== pop =====')
    print(r.lpop(list_key2))
    print(r.lpop(list_key2))
    print(r.lpop(list_key3))


def main():
    push()
    pop()
    r.delete(list_key)
    r.delete(list_key2)
    r.delete(list_key3)


if __name__ == '__main__':
    main()
