# coding: utf-8
import argparse
import datetime


def _datetime(d):
    return datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')


def main():
    # in `class Action(_AttributeHolder)`'s doc
    parser = argparse.ArgumentParser()

    # option_strings
    parser.add_argument("-d", dest="dest")

    # parser.add_argument("--n0", nargs=0)      # store 的时候不能设置
    parser.add_argument("--n1", nargs=1)        # None or [x]
    parser.add_argument("--N1")                 # None or x
    parser.add_argument("--n2", nargs=2)
    # parser.add_argument("--n0", nargs=0)      # store 的时候不能设置
    parser.add_argument("--nx0", nargs='?')     # None or x
    parser.add_argument("--nx1", nargs='+')     # [x]
    parser.add_argument("--nx2", nargs='*')     # [] [x]

    parser.add_argument("--default", default="default")
    parser.add_argument("--type_int", type=int)
    parser.add_argument("--type_datetime", type=_datetime)
    parser.add_argument("--choices", choices=["foo", "bar", "baz"])
    parser.add_argument("--required", required=True)
    parser.add_argument("--help_msg", help="this is my help msg")
    parser.add_argument("--metavar", metavar="metavar_x")

    args = parser.parse_args()

    print("dest: ", args.dest)
    print("n1: ", args.n1)
    print("N1: ", args.N1)
    print("n2: ", args.n2)
    print("nx0: ", args.nx0)
    print("nx1: ", args.nx1)
    print("nx2: ", args.nx2)
    print("default: ", args.default)
    print("type_int: ", args.type_int)
    print("type_datetime: ", args.type_datetime)
    print("choices: ", args.choices)
    print("required: ", args.required)
    print("help_msg: ", args.help_msg)


if __name__ == '__main__':
    main()
