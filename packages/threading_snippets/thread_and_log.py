# coding: utf-8
import logging
import sys
from Queue import Queue
from threading import Thread

worker_size = 10
queue_size = 10

q = Queue(maxsize=queue_size)
logging.basicConfig(
    stream=sys.stdout,   # or filename='xxx.log',
    level=logging.INFO,
    format='%(asctime)s %(name)s %(levelname)s %(module)s %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
# log it


def worker():
    while True:
        item = q.get()
        logging.info(item)
        q.task_done()


def main():

    for i in range(worker_size):
        t = Thread(target=worker)
        t.daemon = True
        t.start()

    print('=== start work ===')
    for i in range(100):
        q.put(i)
    q.join()  # block until all tasks are done
    print('=== end ===')


if __name__ == '__main__':
    main()
