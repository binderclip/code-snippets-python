# coding: utf-8
import argparse


def read_ids_from_file(ids_file):
    ids = []
    with open(ids_file) as f:
        for line in f.readlines():
            ids.append(int(line.strip()))
    return ids


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ids_file", help='select ids file', required=True)
    args = parser.parse_args()
    ids_file = args.ids_file
    ids = read_ids_from_file(ids_file)
    print('{} ids'.format(len(ids)))
    print('{}...'.format(', '.join(map(str, ids[:10]))) if len(ids) > 10 else '{}'.format(', '.join(map(str, ids))))



if __name__ == '__main__':
    main()
