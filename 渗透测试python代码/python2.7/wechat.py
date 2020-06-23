# -*- coding: utf-8 -*-
# 全双工模式
# 0. 定义框架class
# 1. 定义usage函数
# 2. 利用getopt模块获取参数值
# 3. 判断否是启动监听
# 4. 编写客户端、服务端函数
# 5. 利用多线程启动全双工
# 6. 定义发送、接收数据的函数

import socket
import sys
import getopt
from threading import Thread

# 0. 定义框架class
class Wechat:
    # 1. 定义usage函数
    def usage(self):
        print "client usage: python wechat.py -t [target] -p [port]"
        print "server usage: python wechat.py -lp [port]"
        sys.exit()

    # 4. 编写客户端、服务端函数
    def wechat_client(self, target, port):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((target, port))
        print "[*]try connect to the target..."
        print client.recv(1024)

        # 5. 利用多线程启动全双工
        t = Thread(target=self.send_data, args=(client, ))
        t.start()

        c = Thread(target=self.recv_data, args=("server_>", client))
        c.start()

    def wechat_server(self, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('0.0.0.0', port))
        server.listen(1)
        print "[*]Listening on 0.0.0.0:%d" % port
        clien_handle, addr = server.accept()
        print "[*]Accept connect from %s:%d" % (addr[0], addr[1])
        clien_handle.send("[*]connection successfully...")

        # 5. 利用多线程启动全双工
        t = Thread(target=self.send_data, args=(clien_handle, ))
        t.start()

        c = Thread(target=self.recv_data, args=("client_>", clien_handle))
        c.start()


    # 6. 定义发送、接收数据的函数
    def send_data(self, socket):
        while True:
            data = raw_input()
            socket.send(data)
            if 'exit' in data:
                socket.close()
                sys.exit()

    def recv_data(self, who, socket):
        while True:
            recv_len = 1
            response = ""
            while recv_len:
                buffer = socket.recv(4096)
                recv_len = len(buffer)
                response += buffer
                if recv_len < 4096:
                    break
            if response:
                print who, response
            if 'exit' in response:
                socket.close()
                sys.exit()


if __name__ == "__main__":
    port = 0
    listen = False
    help = False
    target = ""
    # 2. 利用getopt模块获取参数值
    opts, args = getopt.getopt(sys.argv[1:], "t:p:lh")
    for o, a in opts:
        if o == "-t":
            target = a
        elif o == "-p":
            port = int(a)
        elif o == "-l":
            listen = True
        elif o == "-h":
            help = True
        else:
            assert False, "Unhandled Option"

    test = Wechat()
    # 3. 判断否是启动监听
    if help:
        test.usage()
    elif not listen:
        test.wechat_client(target, port)
    else:
        test.wechat_server(port)





















