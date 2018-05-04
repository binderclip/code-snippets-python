def main():
    start = 1
    end = 100
    step = 1

    for i in range(start, end + step, step):
        print("{:02d}".format(i))   # 01


if __name__ == '__main__':
    main()
