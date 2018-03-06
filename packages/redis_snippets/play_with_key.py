# coding: utf-8
import redis


def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set('Hello', 'World')
    r.delete("Hello")
    print('Hello, {}!'.format(r.get('Hello')))


if __name__ == '__main__':
    main()
