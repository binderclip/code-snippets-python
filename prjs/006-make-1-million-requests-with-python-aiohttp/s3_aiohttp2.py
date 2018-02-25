import time
import asyncio
import aiohttp
from aiohttp import ClientSession


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.read()


async def bound_fetch(sem, url, session):
    async with sem:
        await fetch(url, session)


async def run(r):
    url = "http://localhost:8080/{}"
    # url = "http://httpbin.org/anything/{}"
    tasks = []
    sem = asyncio.Semaphore(1000)
    connector = aiohttp.TCPConnector(limit=1000)     # 不设置默认是 100
    async with ClientSession(connector=connector) as session:
        for i in range(r):
            task = asyncio.ensure_future(bound_fetch(fetch(url.format(i), session)))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        # for response in responses:
        #     print(response)
        print(f'{len(responses)}')


def main():
    print('=== start ===')
    n = 1000000
    t_start = time.time()

    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(n))
    loop.run_until_complete(future)

    t_end = time.time()
    print('time: {}'.format(t_end - t_start))
    print('=== done ===')


if __name__ == '__main__':
    main()
