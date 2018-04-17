from mypy_extensions import TypedDict


class MovieA(TypedDict):
    name: str
    year: int


MovieB = TypedDict('Movie', {'name': str, 'year': int})


def main():
    m1 = MovieA(name='foo', year=2028)
    m2 = MovieB(name='bar', year=2029)
    print(m1)
    print(m2)
    print(type(m1))
    print(type(m2))


if __name__ == '__main__':
    main()
