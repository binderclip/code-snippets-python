import subprocess


def main():
    ret = subprocess.run(["echo", "hello"], stdout=subprocess.PIPE)
    print(ret)
    print(ret.stdout.strip().decode('utf-8'))


if __name__ == '__main__':
    main()
