import urllib.parse


def main():
    txt = """
西
瓜
"""
    strings = txt.strip().splitlines()
    for s in strings:
        print(f"{s} {urllib.parse.quote_plus(s)}")


if __name__ == '__main__':
    main()

# https://stackoverflow.com/questions/5607551/how-to-urlencode-a-querystring-in-python/9345102#9345102
