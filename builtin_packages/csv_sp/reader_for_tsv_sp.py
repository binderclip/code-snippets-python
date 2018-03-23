import csv


def main():
    with open('some.tsv', 'r', newline='') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            print(row)


if __name__ == '__main__':
    main()


# https://stackoverflow.com/questions/13992971/reading-and-parsing-a-tsv-file-then-manipulating-it-for-saving-as-csv-efficie
