# coding: utf-8
import redis


def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    r.set('Hello', 'World')
    print('Hello, {}!'.format(r.get('Hello')))


if __name__ == '__main__':
    main()
