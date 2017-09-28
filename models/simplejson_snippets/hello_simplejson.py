# coding: utf-8
import simplejson


def dump_loads():
    print("=== dump_loads ===")
    d = {"hello": "world"}
    s = simplejson.dumps(d)
    d2 = simplejson.loads(s)
    print(s)
    print(d2)


def dump_str_escape_test():
    print("=== dump_str_escape_test ===")
    d = {"hello": "world > &"}
    s = simplejson.dumps(d)
    print(s)


def main():
    dump_loads()
    dump_str_escape_test()


if __name__ == '__main__':
    main()
