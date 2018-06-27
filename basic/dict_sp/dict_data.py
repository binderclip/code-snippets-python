def main():
    d = {'foo': 'bar', 'baz': 'qux'}
    print(d.items())
    print(d.values())
    for value in d.values():
        print(value)
    print(d.keys())

if __name__ == '__main__':
    main()
