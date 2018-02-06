# coding: utf-8
import logging
from typing import Sequence, TypeVar, Generic, Iterable
from typing import TypeVar, Generic
from logging import Logger

T = TypeVar('T')


class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log('Set ' + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log('Get ' + repr(self.value))
        return self.value

    def log(self, message: str) -> None:
        self.logger.info('%s: %s', self.name, message)


def zero_all_vars(vars: Iterable[LoggedVar[int]]) -> None:
    for var in vars:
        var.set(0)


def main():
    logging.basicConfig(
        level=logging.INFO,
    )
    logger = logging.getLogger()
    zero_all_vars([LoggedVar(1, 'var1', logger), LoggedVar(2, 'var2', logger)])


if __name__ == '__main__':
    main()
