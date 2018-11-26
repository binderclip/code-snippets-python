import time

from tqdm import tqdm


def main():
    pbar = tqdm(["a", "b", "c", "d"])
    for char in pbar:
        pbar.set_description("Processing %s" % char)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
