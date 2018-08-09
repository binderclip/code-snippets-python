def mean(l):
    return sum(l) / (len(l) or 1)


def main():
    print(mean([3, 3, 4]))
    print(mean([]))


if __name__ == '__main__':
    main()


# https://stackoverflow.com/questions/7716331/calculating-arithmetic-mean-one-type-of-average-in-python
