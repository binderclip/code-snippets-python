try:
    from urlparse import urlparse, urlunparse, parse_qsl
    from urllib import urlencode
except:     # For Python 3
    from urllib.parse import urlencode, urlparse, parse_qsl, urlunparse


def add_params_to_url(url, params):
    url_parts = list(urlparse(url))
    query = dict(parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query)
    return urlunparse(url_parts)


def main():
    url1 = 'http://example.com/search?q=question&t=tag#class1'
    url2 = 'http://example.com/'
    url3 = 'exp.io'
    params = {'lang': 'en', 'tag': 'python'}
    print(urlencode(params))

    print(add_params_to_url(url1, params))
    print(add_params_to_url(url2, params))
    print(add_params_to_url(url3, params))


if __name__ == '__main__':
    main()


# https://stackoverflow.com/questions/2506379/add-params-to-given-url-in-python
