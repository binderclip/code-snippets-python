import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(("httpbin.org", 80))
    s.sendall(b"GET /get HTTP/1.1\r\nHost: httpbin.org\r\n\r\n")
    data = s.recv(4096)
    print(data)
    s.close()


if __name__ == '__main__':
    main()
