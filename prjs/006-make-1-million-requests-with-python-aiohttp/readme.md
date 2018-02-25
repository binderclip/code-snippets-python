
## steps

### s1 一个请求

同步的写法很简单，异步的要复杂很多

### s2 多个请求

即使是异步的，请求数量变多之后总的请求时间也会变多。
单个请求的耗时很长的时候异步的操作会更有优势。

### s3 测试性能

aiohttp server 是有都少请求接收多少，client 则加入了一个默认 100 的限制（ref: https://stackoverflow.com/a/43857526/3936457 ）

请求变到 100w 之后光准备请求都要准备几分钟。

```
# uniform(0.01, 0.8)

# n = 100
python s3_requests.py  0.50s user 0.07s system 1% cpu 39.664 total
python s3_aiohttp.py  0.38s user 0.06s system 37% cpu 1.175 total
# n = 1000
#   limit 100
python s3_aiohttp.py  1.48s user 0.13s system 30% cpu 5.220 total
#   limit 1000
python s3_aiohttp.py  1.62s user 0.22s system 59% cpu 3.101 total
# n = 10000
#   limit 100
python s3_aiohttp.py  12.29s user 0.92s system 27% cpu 47.486 total
#   limit 1000
python s3_aiohttp.py  8.11s user 0.56s system 78% cpu 11.102 total
#   limit 5000
python s3_aiohttp.py  7.32s user 1.19s system 85% cpu 9.948 total
开始出现异常
# n = 100000
#   limit 1000
python s3_aiohttp.py  89.12s user 5.61s system 45% cpu 3:28.38 total
请求期间 client 的 CPU 在 25% 左右
期间 server 的 CPU 在 22% 左右
# n = 1000000
准备期间 client 的 CPU 在 98% 左右，过了几分钟之后 CPU 风扇终于开始转了
```

100w 个请求的时候出现了下面的异常，这个压力看起来太大了，应该在上层也限制下数量分批来请求。

```
=== start ===
Traceback (most recent call last):
  File "s3_aiohttp.py", line 42, in <module>
    main()
  File "s3_aiohttp.py", line 34, in main
    loop.run_until_complete(future)
  File "/usr/local/Cellar/python3/3.6.4_2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/asyncio/base_events.py", line 467, in run_until_complete
    return future.result()
  File "s3_aiohttp.py", line 21, in run
    responses = await asyncio.gather(*tasks)
  File "s3_aiohttp.py", line 8, in fetch
    async with session.get(url) as response:
  File "/Users/clip/.local/share/virtualenvs/code-snippets-python-Q5Kzgw2_/lib/python3.6/site-packages/aiohttp/client.py", line 779, in __aenter__
    self._resp = await self._coro
  File "/Users/clip/.local/share/virtualenvs/code-snippets-python-Q5Kzgw2_/lib/python3.6/site-packages/aiohttp/client.py", line 404, in _request
    break
  File "/Users/clip/.local/share/virtualenvs/code-snippets-python-Q5Kzgw2_/lib/python3.6/site-packages/aiohttp/helpers.py", line 656, in __exit__
    raise asyncio.TimeoutError from None
concurrent.futures._base.TimeoutError
```

## 思考

- 每个请求的平均时间是 t，总请求是 n 个
- 如果同步去请求总耗时相当于是 n * t
- 如果并发的话最快相当于是 t
- 但考虑到实际并发的数量不能太多假设可以有 m 个那么相当于是 n * t / m
- 再考虑到并发带来的开销，实际要慢一些，多加一个系数 x，也就是 n * t / m * x
- 最后 1000 个并发去请求最终可能比同步的去请求快个 200 倍，1h 就变成了 18s，快了很多

## todos

- 发出 100w 个请求
- 和同步的请求做比较耗时、CPU 和 内存占用
- 和使用多线程的同步请求比较耗时、CPU 和 内存占用
- async 语法试错

## refs

- [Making 1 million requests with python-aiohttp](https://pawelmhm.github.io/asyncio/python/aiohttp/2016/04/22/asyncio-aiohttp.html)
