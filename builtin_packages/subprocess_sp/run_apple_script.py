import subprocess


def main():
    ret = subprocess.run(['osascript', '-e', r'''set input_text to text returned of (display dialog "Please input Text here:" default answer "hello world" with title "exchange to python")'''], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(ret)
    print(ret.stdout.strip().decode('utf-8'))


if __name__ == '__main__':
    main()


# https://stackoverflow.com/a/24446693/3936457
