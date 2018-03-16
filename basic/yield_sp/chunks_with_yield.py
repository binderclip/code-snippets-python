def chunks(l, n):
    """ Yield successive n-sized chunks from l. """
    for i in range(0, len(l), n):
        yield l[i:i+n]


def main():
    l = range(0, 10)
    print(list(l))
    for cl in chunks(l, 4):
        print(list(cl))


if __name__ == '__main__':
    main()
