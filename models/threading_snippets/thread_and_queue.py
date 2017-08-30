# coding: utf-8
from Queue import Queue
from threading import Thread

worker_size = 10
queue_size = 10

q = Queue(maxsize=queue_size)


def worker():
    while True:
        item = q.get()
        print(item)
        q.task_done()


def main():

    for i in range(worker_size):
        t = Thread(target=worker)
        t.daemon = True
        t.start()

    print('=== start work ===')
    for i in xrange(100):
        q.put(i)
    q.join()  # block until all tasks are done
    print('=== end ===')


if __name__ == '__main__':
    main()
