# coding: utf-8
import requests
from StringIO import StringIO


def main():
    text = 'hello world!'
    temp = StringIO()
    temp.write(text)
    temp.seek(0)
    temp.name = 'hello.txt'
    files = {
        'file_x': temp
    }
    ret = requests.post('https://httpbin.org/post', files=files)
    print ret.text
    temp.close()


if __name__ == '__main__':
    main()

# https://segmentfault.com/a/1190000005999222
