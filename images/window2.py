import wx


########################################################################
class MainPanel(wx.Panel):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
        #self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.frame = parent

        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        for num in range(4):
            label = "Button %s" % num
            btn = wx.Button(self, label=label)
            sizer.Add(btn, 0, wx.ALL, 5)
            self.Bind(wx.EVT_BUTTON, self.onPlaceImg)
        hSizer.Add((1, 1), 1, wx.EXPAND)
        hSizer.Add(sizer, 0, wx.TOP, 100)
        hSizer.Add((1, 1), 0, wx.ALL, 75)
        self.SetSizer(hSizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

    def onPlaceImg(self, evt):
        btn = evt.GetEventObject().GetLabel()
        print("Label of pressed button = ", btn)
        self.dc = wx.ClientDC(self)
        if not self.dc:
            self.dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            self.dc.SetClippingRect(rect)
        self.dc.Clear()
        bmp = wx.Bitmap("1.bmp")

        self.dc.DrawBitmap(bmp, 0, 0)
    # ----------------------------------------------------------------------
    def OnEraseBackground(self, evt):
        """
        Add a picture to the background
        """
        # yanked from ColourDB.py
        self.dc = evt.GetDC()

        if not self.dc:
            self.dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            self.dc.SetClippingRect(rect)
        self.dc.Clear()
        bmp = wx.Bitmap("0.bmp")
        self.dc.DrawBitmap(bmp, 0, 0)
        print('sobytie')

########################################################################
class MainFrame(wx.Frame):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, None, -1, size=(1168, 760), style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
        panel = MainPanel(self)
        self.Center()


########################################################################
class Main(wx.App):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, redirect=False, filename=None):
        """Constructor"""
        wx.App.__init__(self, redirect, filename)
        dlg = MainFrame()
        dlg.Show()


# ----------------------------------------------------------------------
if __name__ == "__main__":
    app = Main()
    app.MainLoop()