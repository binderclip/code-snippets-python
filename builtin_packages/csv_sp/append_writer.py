import csv


def rows(start, stop):
    for i in range(start, stop):
        yield (i, i * i, ',')


def write_rows(start, stop):
    with open('some.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows(start, stop))


def main():
    write_rows(100, 105)
    write_rows(110, 115)


if __name__ == '__main__':
    main()

