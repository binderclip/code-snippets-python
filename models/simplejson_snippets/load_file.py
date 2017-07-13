# coding: utf-8
import simplejson


def main():
    with open("hello.json") as f:
        s = simplejson.load(f)
        print(s)


if __name__ == '__main__':
    main()
