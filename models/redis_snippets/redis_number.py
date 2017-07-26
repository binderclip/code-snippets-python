# coding: utf-8
import redis


def main():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    print('n: {}'.format(r.get('n')))
    r.set('n', 1)
    print('n: {}'.format(r.get('n')))
    r.incr('n')
    print('n: {}'.format(r.get('n')))
    r.decr('n')
    print('n: {}'.format(r.get('n')))
    r.incr('n', 10)
    print('n: {}'.format(r.get('n')))
    r.decr('n', 2)
    print('n: {}'.format(r.get('n')))
    r.delete('n')


if __name__ == '__main__':
    main()
