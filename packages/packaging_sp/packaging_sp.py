from packaging import version


def main():
    print(version.parse('1.1.2') < (version.parse('1.1.11')))
    print(version.parse('') < (version.parse('1.1.11')))


if __name__ == '__main__':
    main()

# https://stackoverflow.com/questions/11887762/how-do-i-compare-version-numbers-in-python
