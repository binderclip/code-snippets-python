import asyncio


async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('{host} header > {line}'.format(host=host, line=line.decode('utf-8').rstrip()))
    # ignore the body, close the socket
    writer.close()


def main():
    loop = asyncio.get_event_loop()
    tasks = [wget(host) for host in ['httpbin.org', 'requestb.in']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    main()
