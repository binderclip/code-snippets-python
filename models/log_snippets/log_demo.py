# coding: utf-8
import logging


def hello_func():
    logging.info('hello %s', 'world')


def main():
    # config logging
    logging.basicConfig(
        filename='hello.log',
        level=logging.INFO,
        format='%(asctime)s %(name)s %(levelname)s %(module)s %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    # log it
    logging.info('in the main')
    hello_func()

if __name__ == '__main__':
    main()
