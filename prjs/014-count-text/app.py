from collections import defaultdict

import csv


def read_data():
    # f_name = 'foo.txt'
    f_name = 'search_log.txt'
    d = defaultdict(int)
    with open(f_name) as f:
        for line in f.readlines():
            text = line.strip()
            if not text:
                continue
            d[text] += 1
    l = list(d.items())
    l.sort(key=lambda x: x[1], reverse=True)
    return l


def write_date(l):
    f_name = 'top_query_until_2018-09-19.csv'
    with open(f_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(l)


def main():
    l = read_data()
    write_date(l)
    print(l)


if __name__ == '__main__':
    main()
