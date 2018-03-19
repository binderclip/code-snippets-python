import csv


def rows(n):
    for i in range(n):
        yield (i, i * i, ',')


def main():
    with open('some.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows(10))


if __name__ == '__main__':
    main()

