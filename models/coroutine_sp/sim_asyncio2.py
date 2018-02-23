from functools import wraps
from time import time


events_list = []


class Future(object):
    def __init__(self):
        super(Future, self).__init__()
        self.callback = lambda *args: None
        self._done = False

    def set_callback(self, callback):
        self.callback = callback

    def done(self, value=None):
        self._done = True
        self.callback(value)


def _next(gen, future, value=None):
    try:
        try:
            yielded_future = gen.send(value)
        except TypeError:
            # 用于首次，TypeError: can't send non-None value to a just-started generator
            yielded_future = next(gen)

        yielded_future.set_callback(lambda value: _next(gen, future, value))
    except StopIteration as e:
        # return 的结果
        future.done(e.value)


def coroutine(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        future = Future()

        gen = func(*args, **kwargs)
        _next(gen, future)
        return future

    return wrapper


class Event(object):

    def __init__(self, *args, **kwargs):
        self.callback = lambda: None
        events_list.append(self)

    def set_callback(self, callback):
        self.callback = callback

    def is_ready(self):
        result = self._is_ready()

        if result:
            self.callback()

        return result


class SleepEvent(Event):
    def __init__(self, timeout):
        super(SleepEvent, self).__init__()
        self.start_time = time()
        self.timeout = timeout

    def _is_ready(self):
        return time() - self.start_time >= self.timeout


def sleep(timeout):
    future = Future()
    event = SleepEvent(timeout)
    event.set_callback(lambda: future.done())
    return future


@coroutine
def long_add(x, y, duration=1):
    yield sleep(duration)
    return x + y


@coroutine
def task(duration):
    print('start:', time())
    print((yield long_add(1, 2, duration)), time())     # yield 传递的
    print((yield long_add(3, 4, duration)), time())


def run():
    while len(events_list):
        for event in events_list:
            if event.is_ready():
                events_list.remove(event)
                break


def main():
    task(2)
    task(1)
    run()


if __name__ == '__main__':
    main()
