# coding: utf-8


def write_ids_to_file(ids_file, ids):
    with open(ids_file, 'w') as f:
        f.write('\n'.join(map(str, ids)))


def main():
    ids = [3, 5, 7]
    write_ids_to_file('ids2.txt', ids)


if __name__ == '__main__':
    main()
