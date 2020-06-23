# coding=utf-8
# 1. 获取桌面像素尺寸
# 2. 创建DC，也就是布置画布
# 3. 创建位图对象，相当于画笔
# 4. 复制屏幕像素，等同于作画
# 5. 保存图片，释放对象
import win32gui
import win32ui
import win32con
import win32api
import time
def screenshot():
    # 1. 获取桌面像素尺寸
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    # 2. 创建DC，也就是布置画布
    hdesktop = win32gui.GetDesktopWindow()
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    mem_dc = img_dc.CreateCompatibleDC()

    # 3. 创建位图对象，相当于画笔
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)

    # 4. 复制屏幕像素，等同于作画
    # 复制一个从左上角坐标（0，0）开始到长宽（width, height）的图片（相当于整个桌面）到我们的mem_dc中，相当于作画
    mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

    # 5. 保存图片，释放对象
    file_name = "C:\\Users\\times0ng\\Desktop\\" + time.strftime('%Y_%m_%d_%H_%M_%S') + ".bmp"
    screenshot.SaveBitmapFile(mem_dc, file_name)
    print("保存图片: %s" % file_name)

    # 释放对象
    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())

if __name__ == "__main__":
    screenshot()