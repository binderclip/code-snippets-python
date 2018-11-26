import time
from tqdm import tqdm


def main():
    for _ in tqdm(range(70)):
        time.sleep(0.05)

if __name__ == '__main__':
    main()
