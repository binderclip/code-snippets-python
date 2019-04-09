import random


def base36encode(number, alphabet='0123456789abcdefghijklmnopqrstuvwxyz'):
    """Converts an integer to a base36 string."""
    if not isinstance(number, (int)):
        raise TypeError('number must be an integer')

    base36 = ''
    sign = ''

    if number < 0:
        sign = '-'
        number = -number

    if 0 <= number < len(alphabet):
        return sign + alphabet[number]

    while number != 0:
        number, i = divmod(number, len(alphabet))
        base36 = alphabet[i] + base36

    return sign + base36


def base36decode(number):
    return int(number, 36)


def random_yuque_page_id():
    return base36encode(number=random.randint(base36decode('100000'), base36decode('zzzzzz')))  # 让代码简单一点，不要 0 开头的 ID 了，不然还要处理补 0 的逻辑


def main():
    print(random_yuque_page_id())


if __name__ == '__main__':
    main()
