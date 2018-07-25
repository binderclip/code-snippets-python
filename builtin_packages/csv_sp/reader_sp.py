import csv


def main():
    with open('some.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        next(reader)    # pass the first line
        for row in reader:
            print(row)


if __name__ == '__main__':
    main()

# https://stackoverflow.com/questions/11349333/when-processing-csv-data-how-do-i-ignore-the-first-line-of-data
