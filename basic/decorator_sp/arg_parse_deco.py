import base64
import functools
import inspect


def parse_next_cursor_last_id_strict(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(f, *args, **kwargs)
        size = func_args.get('size')
        _next_cursor = base64.urlsafe_b64decode(func_args.get('next_cursor').encode('utf-8'))
        func_args['next_cursor'] = int(_next_cursor) if _next_cursor else 0

        rets = f(**func_args)

        last_id = rets[-1] if rets and len(rets) == size else 0
        if last_id:
            new_next_cursor = base64.urlsafe_b64encode(str(last_id).encode('utf-8')).decode('utf-8')
        else:
            # last_id 为 0 的时候没有新 cursor
            new_next_cursor = ''
        return rets, new_next_cursor
    return wrapper


@parse_next_cursor_last_id_strict
def paged_foo(next_cursor, size):
    last_id = next_cursor
    data = list(range(100, 999))

    # fetch data
    ret = []
    for i in data:
        if i > last_id:
            ret.append(i)
        if len(ret) >= size:
            break

    return ret


def main():
    next_cursor = ''
    while True:
        rets, next_cursor = paged_foo(next_cursor, 10)
        print(rets)
        if not next_cursor:
            break


if __name__ == '__main__':
    main()
