from urllib.parse import urljoin


def test_join_url(url1, url2):
    print(urljoin(url1, url2))


def main():
    test_join_url(
        'example.com',
        'foo',
    )
    test_join_url(
        'http://example.com',
        'foo/bar',
    )
    test_join_url(
        'http://example.com/',
        'foo/bar',
    )
    test_join_url(
        'http://example.com/',
        '/foo/bar',
    )
    test_join_url(
        'http://example.com/',
        'foo/',
    )
    test_join_url(
        'http://example.com/foo',
        'bar/',
    )
    test_join_url(
        'http://example.com/foo/',
        'bar/',
    )
    test_join_url(
        'http://example.com/foo',
        '/bar/',
    )
    test_join_url(
        'http://example.com/foo',
        '../bar/',
    )
    test_join_url(
        'http://example.com/foo/bar',
        '../baz/',
    )


if __name__ == '__main__':
    main()
