class Base:
    class Meta:
        foo = 'f'
        bar = 'b'


class Fancy(Base):
    class Meta:
        bar = 'ar'
        baz = 'baz'


def main():
    print(Base.Meta.foo, Base.Meta.bar)
    # print(Fancy.Meta.foo, Fancy.Meta.bar, Fancy.Meta.baz)  # AttributeError: type object 'Meta' has no attribute 'foo'
    print(Fancy.Meta.bar, Fancy.Meta.baz)


if __name__ == '__main__':
    main()

# https://stackoverflow.com/questions/10344197/how-does-djangos-meta-class-work
