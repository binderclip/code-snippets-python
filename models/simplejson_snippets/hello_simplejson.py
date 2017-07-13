# coding: utf-8
import simplejson


def main():
    d = {"hello": "world"}
    s = simplejson.dumps(d)
    d2 = simplejson.loads(s)
    print(s)
    print(d2)


if __name__ == '__main__':
    main()
