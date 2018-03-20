import fire


def main(file):
    with open(file, 'r') as f:
        data = f.read()

    with open(f'out-{file}', 'wb') as f:
        f.write(b'\xef\xbb\xbf')
        f.write(data.encode('utf-8'))


if __name__ == '__main__':
    fire.Fire(main)

# https://segmentfault.com/a/1190000004321605
