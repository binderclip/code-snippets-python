# coding: utf-8
import simplejson


def main():
    with open("hello.json") as f:
        s = simplejson.load(f)
        print(s)
    with open("hello.json", 'w') as f:
        simplejson.dump({}, f)


if __name__ == '__main__':
    main()
