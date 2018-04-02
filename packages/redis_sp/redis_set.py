import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)


def main():
    key = 'foo'
    print(r.get(key))
    r.set(key, 'a', xx=True)
    print(r.get(key))
    r.set(key, 'b', nx=True)
    print(r.get(key))
    r.set(key, 'c', nx=True)
    print(r.get(key))
    r.set(key, 'd', xx=True)
    print(r.get(key))


if __name__ == '__main__':
    main()
