# coding: utf-8
import argparse


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-n", "--none", help="default store action")    # 同 store
    parser.add_argument("-s", "--store", help="store action", action="store")   # 只存储最后一次设置
    parser.add_argument("-c", "--store_const", help="store_const action", action="store_const", const="CONST")  # 设置的话使用 CONST
    parser.add_argument("-t", "--store_true", help="store_true action", action="store_true")    # 设置为 True，否则为 False
    parser.add_argument("-f", "--store_false", help="store_false action", action="store_false") # 设置为 False，否则为 True
    parser.add_argument("-a", "--append", help="append action", action="append")    # 得到一个数组
    parser.add_argument("-A", "--append_const", help="append_const action", action="append_const", const="APPEND_CONST")    # 得到 const 的数组
    parser.add_argument("-C", "--count", help="count action", action="count")   # 设置的次数
    parser.add_argument("-H", "--HELP", help="help action", action="help")   # 打印帮助信息然后退出
    parser.add_argument("-v", "--version", help="version action", action="version", version="V0.0.1")   # 打印填写的版本信息
    # parser.add_argument("-p", "--parsers", help="parsers action", action="parsers")   # 不知道怎么用

    args = parser.parse_args()

    print("none: ", args.none)
    print("store: ", args.store)
    print("store_const: ", args.store_const)
    print("store_true: ", args.store_true)
    print("store_false: ", args.store_false)
    print("append: ", args.append)
    print("append_const: ", args.append_const)
    print("count: ", args.count)
    # print("help: ", args.HELP)    # 不会被设置
    # print("version: ", args.version)  # 不会被设置
    # print("parsers: ", args.parsers)  # 不知道


if __name__ == '__main__':
    main()
