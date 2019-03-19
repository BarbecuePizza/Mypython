# -*-coding:utf-8 -*-
# !/usr/local/bin/python3

import socket
import threading
import time

def socket_sever():
    sever_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    sever_socket.bind((host, port))
    sever_socket.listen(5)

    while True:
        sock, addr=sever_socket.accept()
        t=threading.Thread(target=tcp_link,args=(sock,addr))
        t.start()

def tcp_link(sock,addr):
    print('Accept new connection from %s:%s...'%addr)
    sock.send('welcome to python socket!! 已经连接上服务端'.encode('utf-8'))
    while True:
        data=sock.recv(1024)
        time.sleep()
        if not data or data.decode('utf-8')=='exit':
            break
        sock.send('Hello,%s!'%data.decode('utf-8').encode('utf-8'))
    sock.close()
    print('Connection from %s closed.'%addr)

def main():
    socket_sever()

if __name__ == '__main__':
    main()

