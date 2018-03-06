import threading
import asyncio


@asyncio.coroutine
def hello():
    print(f'Hello World! ({threading.current_thread()})')
    # 异步调用 asyncio.sleep(1):
    yield from asyncio.sleep(1)
    print(f'Hello again! ({threading.current_thread()})')


def main():
    # 获取 EventLoop
    loop = asyncio.get_event_loop()
    # 执行 coroutine
    loop.run_until_complete(hello())

    tasks = [hello(), hello(), hello()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    main()
