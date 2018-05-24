from enum import Enum


class ErrorCode(tuple, Enum):
    common = (1000, '请求错误')
    user_not_exist = (1001, '用户不存在')


def main():
    e1 = ErrorCode.common
    print(e1)
    print(e1.name)
    print(e1.value)
    print(e1[0], e1[1])


if __name__ == '__main__':
    main()
