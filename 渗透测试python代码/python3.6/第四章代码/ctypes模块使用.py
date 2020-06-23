# coding=utf-8
# python 3.6
# DLL文件即动态链接库文件，是一种可执行文件，它允许程序共享执行特殊任务所必需的代码和其他资源。
# Windows提供的DLL文件中包含了允许基于Windows的程序在Windows环境下操作的许多函数和资源。

from ctypes import *

# 调用user32.dll kernel32.dll psapi.dll
user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi

# 调用user32.dll的GetForegroundWindow 函数，返回目标桌面上当前活动窗口的句柄，然后通过控制句柄来操作数据
# 句柄类似于指针，我们可以通过调用句柄来调用它所代表的资源
hwnd = user32.GetForegroundWindow()

# pid=c_ulong(0)相当于c语言定义一个unsign long类型的变量，赋值为0,用于接收后面获取到的进程ID；
# byref相当于c语言的&符，用来取指针地址，所以addr就存储着32位值的地址;
pid = c_ulong(0)
addr = byref(pid)

# user32.GetWindowThreadProcessId(hwnd, byref(pid))返回当前窗口进程ID给pid
# pid是ctypes的数据类型，用pid.value转换为python类型
user32.GetWindowThreadProcessId(hwnd, byref(pid))
process_id = pid.value

# 申请一个512byte 大小的内存空间，buffer相当于c语言中的变量，byref(buffer)代表指针
buffer = create_string_buffer(b"\x00", 512)

# kernel32.OpenProcess(0x400 | 0x10, False, pid) 打开pid对应的进程，返回一个进程句柄
# 第一个参数代表访问权限，0x10是进程信息，0x400没查到具体代表什么权限
# 第二个参数代表继承标志
# 第三个参数是进程ID，使用ctypes格式
h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)

# the return value specifies the length of the string copied to the buffer, in characters.
# psapi.GetModuleBaseNameA(h_process, None, byref(buffer), 512) 将进程的名称拷贝到缓冲区内（buffer）
# 第一个参数指定进程的句柄
# 第二个参数指定模块句柄，这里不指定
# 第三个参数指定缓冲区的指针，缓冲区用来接收进程的名称
# 第四个参数指定缓冲区大小
psapi.GetModuleBaseNameA(h_process, None, byref(buffer), 512)
process_name = buffer.value.decode()

# 关闭句柄
kernel32.CloseHandle(hwnd)
kernel32.CloseHandle(h_process)

