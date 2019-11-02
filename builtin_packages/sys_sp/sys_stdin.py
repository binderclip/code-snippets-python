import sys


def main():
    t = sys.stdin.read()  # will block if no std input
    print(t)


if __name__ == '__main__':
    main()

# https://stackoverflow.com/questions/1450393/how-do-you-read-from-stdin/1450398#1450398
# sys.stdin is a file-like object on which you can call functions read or readlines if you want to read everything or
# you want to read everything and split it by newline automatically. (You need to import sys for this to work.)
