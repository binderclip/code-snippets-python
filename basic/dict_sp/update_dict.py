
def main():
    d1 = {
        'foo': 'a',
        'bar': 'b',
    }
    print(d1)
    d1['foo'] = 'aa'
    print(d1)
    d2 = {
        'bar': 'bbb',
    }
    d1.update(d2)
    print(d1)
    print(d1.pop('foo'))
    print(d1)


if __name__ == '__main__':
    main()
