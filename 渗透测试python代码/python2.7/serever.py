# -*- coding: utf-8 -*-
# 1. 创建socket套接字
# 2. 绑定IP和端口
# 3. 进行监听
# 4. 接收、发送数据

import socket

def main(target, port):
    # 1. 创建socket套接字
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 绑定IP和端口号
    server.bind((target, port))

    # 3. 启动监听
    server.listen(10)
    print "[*] 启动监听 %s:%d" % (target, port)

    # 接收和发送数据
    client, addr = server.accept()

    print "[*] 接收到来自在 %s:%d" % (addr[0], addr[1])
    response = client.recv(1024)
    print response
    client.send("success to connection...")
    client.close()


if __name__ == "__main__":
    target = '0.0.0.0'
    port = 4444
    main(target, port)