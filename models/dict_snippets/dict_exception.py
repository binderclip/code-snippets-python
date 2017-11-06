# coding: utf-8


def main():
    d = {"a": "aa"}
    try:
        d['b']  # KeyError: 'b'
    except Exception as e:
        print(e)
        raise e



if __name__ == '__main__':
    main()
