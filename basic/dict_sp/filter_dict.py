
def filter_dict_none(d):
    return {k: v for k, v in d.items() if v is not None}


def main():
    d = {
        'foo': 'bar',
        'baz': None,
    }
    d = filter_dict_none(d)
    print(d)


if __name__ == '__main__':
    main()
