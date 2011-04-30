import win32com.client
import win32ui, win32api, win32con,win32gui
from PIL import ImageGrab

class Bot():
    '''Generic Class for writing Win32 screen-scraping bots'''
    
    def __init__(self,title):
        self.title = title
        (self.left,self.top,self.right,self.bottom) = win32ui.FindWindow(None, title).GetWindowRect()
        self.hwin = win32ui.FindWindow(None, title).GetSafeHwnd()
        self.shell = win32com.client.Dispatch("WScript.Shell")
        self.shell.AppActivate(title)

    def click(self,(x,y)):
        '''clicks w/ offsets'''
        x,y = x+self.left,y+self.top
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

    def capture(self,):
        im = ImageGrab.grab((self.left,self.top,self.right,self.bottom))
        return im

    def sendKeys(self,keys):
        self.shell.SendKeys(keys)

if __name__ == "__main__":
    a = Bot("StarCraft II")
    a.capture()




    # im.save('C:\Users\Cory\Pictures\screenshot.png')
    #print 'image saved'




