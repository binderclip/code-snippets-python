import time
import asyncio
from aiohttp import ClientSession


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.read()


async def run(r):
    url = "http://httpbin.org/anything/{}"
    # url = "https://www.baidu.com/s?wd={}"
    tasks = []
    async with ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        # for response in responses:
        #     print(response)
        print(f'{len(responses)}')


def main():
    print('=== start ===')
    t_start = time.time()

    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(run(30))
    loop.run_until_complete(future)

    t_end = time.time()
    print('time: {}'.format(t_end - t_start))
    print('=== done ===')


if __name__ == '__main__':
    main()
