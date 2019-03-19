# -*-coding:utf-8 -*-
# !/usr/local/bin/python3
import socket


def socket_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    s.connect((host, port))
    print(s.recv(1024).decode('utf-8'))
    for data in ['小萌', '小智', '小强']:
        s.send(data.encode('utf-8'))
        print(s.recv(1024).decode('utf-8'))
    s.send(b'exit')
    s.close()


def main():
    socket_client()


if __name__ == '__main__':
    main()
