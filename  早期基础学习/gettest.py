# -*-coding:utf-8 -*-
#!/usr/local/bin/python3

from urllib import request

def get_request():
    with request.urlopen('http://www.baidu.com') as f:
        data = f.read()
        print('Status:',f.status,f.reason)
        for k ,v in f.getheaders():
            print('%s:%s'%(k,v))
    print('Data:',data.decode('utf-8'))

def main():
    get_request()

if __name__ == '__main__':
    main()