# coding: utf-8
from urlparse import urljoin


def test_join_url(url1, url2):
    print(urljoin(url1, url2))


def main():
    test_join_url(
        'http://example.com',
        'foo',
    )


if __name__ == '__main__':
    main()
