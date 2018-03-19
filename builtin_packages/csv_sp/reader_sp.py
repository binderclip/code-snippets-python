import csv


def main():
    with open('some.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)


if __name__ == '__main__':
    main()

