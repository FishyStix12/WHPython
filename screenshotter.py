#!/usr/bin/env python

import platform
import base64
if platform.system() == 'Windows':
    import win32api
    import win32con
    import win32gui
    import win32ui

elif platform.system() == 'Linux':
    from Xlib import display

def get_dimensions():
    # Defining a function to get the screen dimensions

    if platform.system() == 'Windows':
        # Checking if the current operating system is Windows

        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        # Getting the width of the virtual screen in pixels
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        # Getting the height of the virtual screen in pixels
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        # Getting the x-coordinate of the left side of the virtual screen
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
        # Getting the y-coordinate of the top side of the virtual screen
        return (width, height, left, top)
        # Returning the screen dimensions as a tuple

    elif platform.system() == 'Linux':
        # Checking if the current operating system is Linux

        screen = display.Display().screen()
        # Creating a display object to access the X server display information
        width = screen.width_in_pixels
        # Getting the width of the screen in pixels
        height = screen.height_in_pixels
        # Getting the height of the screen in pixels
        return (width, height, 0, 0)
        # Returning the screen dimensions as a tuple with 0 coordinates for left and top

    else:
        # Handling the case when the platform is not supported
        raise NotImplementedError("This platform is not supported")

def screenshot(name='screenshot'):
    # Defining a function to take a screenshot

    if platform.system() == 'Windows':
        # Checking if the current operating system is Windows

        hdesktop = win32gui.GetDesktopWindow()
        # Getting the handle to the desktop window
        width, height, left, top = get_dimensions()
        # Getting the screen dimensions

        desktop_dc = win32gui.GetWindowDC(hdesktop)
        # Getting the device context (DC) for the entire desktop
        img_dc = win32ui.CreateDCFromHandle(desktop_dc)
        # Creating a DC object from the desktop DC
        mem_dc = img_dc.CreateCompatibleDC()
        # Creating a memory DC compatible with the desktop DC

        screenshot = win32ui.CreateBitmap()
        # Creating a bitmap object for the screenshot
        screenshot.CreateCompatibleBitmap(img_dc, width, height)
        # Creating a compatible bitmap for the screenshot
        mem_dc.SelectObject(screenshot)
        # Selecting the bitmap into the memory DC
        mem_dc.BitBlt((0,0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
        # Performing a bit-block transfer of the color data from the desktop DC to the memory DC
        screenshot.SaveBitmapFile(mem_dc, f'{name}.bmp')
        # Saving the bitmap to a file

        mem_dc.DeleteDC()
        # Deleting the memory DC
        win32gui.DeleteObject(screenshot.GetHandle())
        # Deleting the screenshot object

def run():
    # Defining a function to run the script

    screenshot()
    # Taking a screenshot
    with open('screenshot.bmp', 'rb') as f:
        img = f.read()
        # Reading the screenshot image data
    return base64.b64encode(img)
    # Encoding the image data in base64 format

if __name__ == '__main__':
    # Checking if the script is being run directly

    screenshot()
    # Taking a screenshot
