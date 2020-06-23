'''
# bytes 和 str 之间的转换
test = "hello world"
print(type(test))

byte = test.encode('utf-8')
print(type(byte))

string = byte.decode()
print(type(string))
'''

#import sys
#print(sys.argv[1:])

import sys
import getopt
# opts 接收的是命令行传入的短选项和值，args 接收额外的值
# o 变量就保存了我们的短选项， a保存了短选项指定的值
opts, args = getopt.getopt(sys.argv[1:], "a:b:c")
for o, a in opts:
    print(o, a)

