from contextlib import contextmanager


@contextmanager
def custom_open(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()


with custom_open('file') as f:
    contents = f.read()
