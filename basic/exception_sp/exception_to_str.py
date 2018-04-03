def main():
    print('Hello')
    try:
        # raise Exception('hello')
        raise Exception('foo', 'bar')
    except Exception as e:
        print(e)
        print(repr(e))


if __name__ == '__main__':
    main()


# str -> https://github.com/python/cpython/blob/master/Objects/exceptions.c#L104
# repr -> https://github.com/python/cpython/blob/master/Objects/exceptions.c#L117