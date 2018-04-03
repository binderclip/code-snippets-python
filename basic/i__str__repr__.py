class Foo(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        print("=== __repr__ ===")
        return f'Foo(id={self.id}, name={self.name})'

    def __str__(self):
        print("=== __str__ ===")
        return f'Foo(id={self.id}, name={self.name})'


def main():
    foo = Foo(1, 'fooo')
    print(foo)
    print(str(foo))
    print([foo])
    print(str([foo]))


if __name__ == '__main__':
    main()
