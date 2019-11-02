import re


def main():
    s = "a 12:22,b 32:00xc,34:0sdf"
    print(re.findall(r'\d\d:\d\d', s))


if __name__ == '__main__':
    main()

# https://stackoverflow.com/questions/4697882/how-can-i-find-all-matches-to-a-regular-expression-in-python