import uuid


def get_a_part_or_uuid():
    return str(uuid.uuid4())[:16]


def main():
    pus = []
    for i in range(10000000):
        pus.append(get_a_part_or_uuid())
    print(len(pus))     # 10000000
    s_pus = set(pus)
    print(len(s_pus))   # 10000000


if __name__ == '__main__':
    main()
