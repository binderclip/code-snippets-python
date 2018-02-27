import pytest


def f():
    raise SystemExit(1)


def test_exception():
    with pytest.raises(SystemExit):
        # 如果不抛异常会报错 Failed: DID NOT RAISE <class 'SystemExit'>
        f()
