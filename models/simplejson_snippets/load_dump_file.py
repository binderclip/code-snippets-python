# coding: utf-8
import codecs
import simplejson


def load_dump_test():
    print('''=== load_dump_test ===''')
    with open("hello.json") as f:
        s = simplejson.load(f)
        print(s)
    with open("hello.json", 'w') as f:
        simplejson.dump({"hello": "world"}, f)


def load_dump_unicode_test():
    print('''=== load_dump_unicode_test ===''')
    file_name = "hello_u.json"
    data = {"hello": "世界"}
    with open(file_name) as f:
        s = simplejson.load(f)
        print(s)
    # with open(file_name, 'w') as f:
        # simplejson.dump(data, f, ensure_ascii=False)    # UnicodeEncodeError
    with codecs.open(file_name, 'w', 'utf-8') as f:
        simplejson.dump(data, f, ensure_ascii=False)


def main():
    load_dump_test()
    load_dump_unicode_test()


if __name__ == '__main__':
    main()


# https://stackoverflow.com/questions/17665213/getting-a-unicodeencodeerror-when-trying-to-write-a-json-file
