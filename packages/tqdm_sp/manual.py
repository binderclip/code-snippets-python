import time

from tqdm import tqdm


def main():
    pbar = tqdm(total=100)
    for i in range(10):
        pbar.update(10)
        time.sleep(0.5)
    pbar.close()


if __name__ == '__main__':
    main()
