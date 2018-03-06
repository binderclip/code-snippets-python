from time import time


events_list = []


class Event(object):

    def __init__(self, *args, **kwargs):
        # 在一个统一的地方做登记，用于调度
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
        super(SleepEvent, self).__init__(timeout)
        self.timeout = timeout
        self.start_time = time()

    def _is_ready(self):
        return time() - self.start_time >= self.timeout


def sleep(timeout):
    # 是一些阻塞的事件，阻塞事件结束之后会继续执行后面的东西
    return SleepEvent(timeout)


def task(name):
    # 会生成一个迭代器，被执行 next 的时候向后走一次 yield
    print(name, 1)
    yield sleep(1)
    print(name, 2)
    yield sleep(2)
    print(name, 3)


def run(tasks):
    for task in tasks:
        # 启动一下
        _next(task)

    while len(events_list):
        for event in events_list:
            if event.is_ready():
                events_list.remove(event)
                break


def _next(task):
    # 让 task 执行一个 yield
    # yield 到的是一个记录，这个记录可以用于判断是不是要继续
    # 这里预先设置一个回调，使得继续的话是继续执行本函数
    # 如果 task 中已经没有 yield 了就结束不再设置回调
    try:
        event = next(task)      # 靠 next 来让真正的 task 继续执行
        event.set_callback(lambda: _next(task))     # 1
    except StopIteration:
        pass


def main():
    run((task('hsfzxjy'), task('Jack')))


if __name__ == '__main__':
    main()
