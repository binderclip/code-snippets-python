# coding: utf-8
import re
import urllib.request
from bs4 import BeautifulSoup


def is_a_valid_url(s):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return bool(regex.search(s))


def get_title_from_url(url):
    if not is_a_valid_url(url):
        return ''
    soup = BeautifulSoup(urllib.request.urlopen(url), 'html.parser')
    return soup.title.string


def main():
    url = 'https://mp.weixin.qq.com/s/uqPPe_YdG7c0JdSHPng_MQ'
    print(u"{}\n{}".format(get_title_from_url(url), url))


if __name__ == '__main__':
    main()
