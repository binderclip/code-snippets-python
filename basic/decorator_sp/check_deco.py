import functools
import inspect


# 方法原本的属性会被覆盖
def check_is_admin_1(f):
    def wrapper(*args, **kwargs):
        if kwargs.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper


def check_is_admin(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        func_args = inspect.getcallargs(f, *args, **kwargs)     # 会处理掉 args 和 kwargs 的对齐问题
        if func_args.get('username') != 'admin':
            raise Exception("This user is not allowed to get food")
        return f(*args, **kwargs)
    return wrapper


class Store(object):

    def __init__(self):
        self.storage = {
            'apple': 3,
        }

    @check_is_admin
    def get_food(self, username, food):
        return self.storage.get(food)

    @check_is_admin
    def put_food(self, username, food):
        self.storage.set(food)


def main():
    s = Store()
    print(s.get_food(username='admin', food='apple'))
    print(s.get_food('admin', 'apple'))
    # print(s.get_food(username='foo', food='apple'))     # Exception: This user is not allowed to get food


if __name__ == '__main__':
    main()
