import requests


def retries(times=3):
    def wrap(func):
        def r(*args, **kw):
            t = 0
            while True:
                try:
                    return func(*args, **kw)
                except requests.exceptions.ConnectTimeout as e:
                    t += 1
                    if t < times:
                        print('retry {}'.format(t))
                    else:
                        raise e
        return r
    return wrap


@retries()
def make_a_get():
    return requests.get('http://httpbin.org/get', timeout=(0.3, 2))


def main():
    print(make_a_get())


if __name__ == '__main__':
    main()
