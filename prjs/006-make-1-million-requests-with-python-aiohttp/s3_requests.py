import requests
import time


def fetch(i, session):
    # url = f"http://localhost:8080/{i}"
    url = f"http://httpbin.org/anything/{i}"
    return session.get(url)


def main():
    print('=== start ===')
    n = 100
    t_start = time.time()

    texts = []
    s = requests.Session()
    for i in range(n):
        texts.append(fetch(i, s).text)

    t_end = time.time()
    print('time: {}'.format(t_end - t_start))

    # for text in texts:
    #     print(text)
    print(f'{len(texts)}')
    print('=== done ===')


if __name__ == '__main__':
    main()
