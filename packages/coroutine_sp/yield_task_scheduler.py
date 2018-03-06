from collections import deque


def task(name, times):
    for i in range(times):
        yield i
        print(name, i)


class Runner(object):

    def __init__(self, tasks):
        self.tasks = deque(tasks)

    def next(self):
        return self.tasks.pop()

    def run(self):
        while len(self.tasks):
            task = self.next()
            try:
                i = next(task)
                print(f'>>> i:{i}')
            except StopIteration:
                pass
            else:
                self.tasks.appendleft(task)


def main():
    Runner([
        task('hsfzxjy', 5),
        task('Jack', 4),
        task('Bob', 6)
    ]).run()


if __name__ == '__main__':
    main()
