# coding: utf-8
import json


def dump_loads():
    print("=== dump_loads ===")
    d = {"hello": "world"}
    s = json.dumps(d)
    d2 = json.loads(s)
    print(s)
    print(d2)


def dump_str_escape_test():
    print("=== dump_str_escape_test ===")
    d = {"hello": "world > &"}
    s = json.dumps(d)
    print(s)


def test_ensure_ascii():
    print("=== test_ensure_ascii ===")
    d = {'hello': '世界'}
    print(json.dumps(d))
    print(json.dumps(d, ensure_ascii=False))


def test_pretty_printed():
    print("=== test_pretty_printed ===")
    d = {'a': {'b': 'c'}}
    print(json.dumps(d))
    print(json.dumps(d, indent=4))
    print(json.dumps(d, indent="    "))


def test_compact_printed():
    print("=== test_compact_printed ===")
    d = {'a': {'b': ['c', 'd']}}
    print(json.dumps(d))
    print(json.dumps(d, separators=None))
    print(json.dumps(d, separators=(', ', ': ')))
    print(json.dumps(d, separators=(',', ':')))


def main():
    dump_loads()
    dump_str_escape_test()
    test_ensure_ascii()
    test_pretty_printed()
    test_compact_printed()


if __name__ == '__main__':
    main()
