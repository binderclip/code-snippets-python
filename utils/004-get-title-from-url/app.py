# coding: utf-8
import urllib2
from bs4 import BeautifulSoup


def main():
    url = 'https://mp.weixin.qq.com/s/uqPPe_YdG7c0JdSHPng_MQ'
    soup = BeautifulSoup(urllib2.urlopen(url), 'html.parser')
    print(u"{}\n{}".format(soup.title.string, url))


if __name__ == '__main__':
    main()
