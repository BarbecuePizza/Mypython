# -*- coding: utf-8 -*-
# 1. 首先定义usage函数
# 2. 利用getopt模块获取命令行参数
# 3. 区分客户端和服务器端
# 4. 编写客户端函数和服务端函数
# 5. 编写文件上传函数、文件下载函数

import sys
import socket
import getopt
import time
upfile = ""

def main():
    global upfile
    help = False
    listen = False
    target = ""
    port = 0

    # 2. 利用getopt获取命令行参数
    opts, args = getopt.getopt(sys.argv[1:], "t:p:u:lh")
    for o, a in opts:
        if o == "-t":
            target = a
        elif o == "-p":
            port = int(a)
        elif o == "-l":
            listen = True
        elif o == "-u":
            upfile = a
        elif o == "-h":
            help = True
        else:
            assert  False, "Unhandled Option"

    if help:
        usage()

    # 3. 区分客户端和服务器端
    if not listen:
        client_handle(target, port)
    else:
        server_handle(port)

# 4. 编写客户端函数
def client_handle(target, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target, port))
    client.send(upfile)
    time.sleep(1)
    upload_file(client)
    client.close()

# 5. 编写上传文件函数
def upload_file(client):
    f = open(upfile, 'rb')
    data = f.read()
    client.send(data)
    f.close()

# 4_ . 编写服务端函数
def server_handle(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(1)
    print "[*]listening on 0.0.0.0:%d" % port
    while True:
        client_socket, addr = server.accept()
        download_file(client_socket)

# 5_ . 编写文件下载函数
def download_file(client_socket):
    filename = client_socket.recv(1024)
    print "[*]Receive the file: %s" % filename
    file_buffer = ""
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        else:
            file_buffer += data
    f = open(filename, 'wb')
    f.write(file_buffer)
    f.close()



def usage():
    print "python filename.py -t [target] -p [port] -u [uploadfile]"
    print "python filename.py -lp [port]"
    sys.exit()

if __name__ == "__main__":
    main()
