import wx
import os

APP_SIZE_X = 700
APP_SIZE_Y = 300


class MainWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Agent-Based Model of ResidentialDevelopment", size = (APP_SIZE_X, APP_SIZE_Y))

        self.panel = wx.Panel(self,-1)
        self.imageFile = os.path.abspath("admin0.png")  # provide a diff file name in same directory/path
        self.bmp = wx.Image(self.imageFile,wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self.panel, -1, self.bmp, (20,20), (160,220))

        button42 = wx.Button(self.panel, -1, "Read", pos=(240,20))
        self.Bind(wx.EVT_BUTTON, self.OnRead,button42)

    def OnRead(self,event):
        self.imageFile1=os.path.abspath("0.bmp") # you have to provide a diff image file name
        self.bmp = wx.Image(self.imageFile1,wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        wx.StaticBitmap(self.panel, -1, self.bmp, (20,20), (160,220))

if __name__ == "__main__":
    app = wx.App()
    dlg = MainWindow()
    dlg.Show()
    app.MainLoop()
