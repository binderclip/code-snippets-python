import json
import csv


def load_json(name):
    with open(name) as f:
        s = json.load(f)
        return s


def ds_2_rows(d1, d2, d3):
    rows = [(k, v, d2.get(k, ""), d3.get(k, "")) for (k, v) in d1.items()]
    return [('key', 'zh', 'en', 'jp')] + rows


def dump_csv(rows):
    with open('out.csv', 'w', newline='') as f:
        writer = csv.writer(f, dialect='excel')
        writer.writerows(rows)


def main():
    dz = load_json("zh-CN.json")
    de = load_json("en-US.json")
    dj = load_json("ja-JP.json")
    rows = ds_2_rows(dz, de, dj)
    # print(rows)
    dump_csv(rows)


if __name__ == '__main__':
    main()
