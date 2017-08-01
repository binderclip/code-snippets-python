# coding: utf-8
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)


def number():
    print('===== number =====')
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


def str_and_number():
    print('===== str_and_number =====')
    print('n: {}'.format(r.get('n')))
    r.set('n', 1)
    print('n: {}'.format(r.get('n')))
    print('type n: {}'.format(type(r.get('n'))))
    r.set('n', '1')
    print('n: {}'.format(r.get('n')))
    print('type n: {}'.format(type(r.get('n'))))
    print('incr n: {}'.format(r.incr('n')))
    print('n: {}'.format(r.get('n')))
    # r.set('n', 1.1)
    # r.incr('n')     # value is not an integer or out of range
    # r.set('n', 'x')
    # r.incr('n')     # value is not an integer or out of range
    r.delete('n')


def main():
    number()
    str_and_number()


if __name__ == '__main__':
    main()
