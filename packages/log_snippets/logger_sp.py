# coding: utf-8
import logging


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(name)s %(levelname)s %(module)s %(funcName)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logger = logging.getLogger()
    logger.info('hello world i')
    logger.warning('hello world w')

if __name__ == '__main__':
    main()
