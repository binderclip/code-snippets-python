import socket


def main():
    HOST = '127.0.0.1'  # 标准的回环地址 (localhost)
    PORT = 65432        # 监听的端口 (非系统级的端口: 大于 1023)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            # 用了 context manager 之后不用再手动关闭
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break  # 返回空对象时结束
                conn.sendall(data)


if __name__ == '__main__':
    main()
