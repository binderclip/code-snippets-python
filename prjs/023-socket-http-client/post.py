import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(("httpbin.org", 80))
    print("== after connect")
    s.sendall(b'POST /post HTTP/1.1\r\nHost: httpbin.org\r\n\r\n{"foo": "bar"}')
    # b'HTTP/1.1 503 Service Unavailable.\r\nContent-length:0\r\n\r\n'
    # 如果不设置 Content-length 的话似乎 post 就不能携带内容了，server 可能会认为没有 body，但是又来了 body 就会出错
    print("== after sendall")
    s.shutdown(1)
    print("== after shutdown")
    data = s.recv(4096)
    print(data)
    s.close()


if __name__ == '__main__':
    main()
