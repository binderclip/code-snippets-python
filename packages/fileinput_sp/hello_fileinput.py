import fileinput


def main():
    lines = []
    for line in fileinput.input():
        lines.append(line)
        print('OK')
    print('=== end ===')
    print(''.join(lines))


if __name__ == '__main__':
    main()
