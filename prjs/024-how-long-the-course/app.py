import sys
import re


def main():
    text = sys.stdin.read()
    time_strs = re.findall(r'\d\d:\d\d', text)
    seconds = 0
    for time_str in time_strs:
        ms, ss = time_str.split(":")
        seconds += int(ms) * 60 + int(ss)
    print(seconds // 60)


if __name__ == '__main__':
    main()
