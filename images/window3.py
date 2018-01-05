import wx

#######################################################################

class MyPanel(wx.Panel):

    def __init__(self, parent, state, button_image, background_image):
        wx.Panel.__init__(self, parent=parent)

        print( "(debug) MyPanel.__init__: state:", state)

        self.parent = parent
        self.state  = state

        self.button_image = button_image
        self.background_image = background_image


        #self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)

        vsizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.buttonOne=wx.Image("C:/Users/Dimon/PycharmProjects/Game2/8.bmp", wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        self.buttonImage = wx.Image(button_image, wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button = wx.BitmapButton(self, -1, self.buttonImage, pos=(300,150))

        self.button.Bind(wx.EVT_LEFT_DOWN, self.buttonClick)

        self.backgroundImage = wx.Bitmap(self.background_image)

        vsizer.Add(self.button, 0, wx.ALL, 5)

        hSizer.Add((1,1), 1, wx.EXPAND)
        hSizer.Add(vsizer, 0, wx.TOP, 100)
        hSizer.Add((1,1), 0, wx.ALL, 75)

        self.SetSizer(hSizer)
        bmp = wx.Image("80.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        self.button2 = wx.BitmapButton(self, -1, bmp, pos=(590, 575), style=wx.NO_BORDER)
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button2)

    def OnClick(self, event):
        # self.Destroy() #  так как принадлежит панели то и удаляет "дестроит" панель

        self.parent.ChangePanel()
    def buttonClick(self, evt):
        print("(debug) MyPanel.buttonClick")
        self.parent.ChangePanel()

    def OnEraseBackground(self, evt):
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        dc.DrawBitmap(self.backgroundImage, 0, 0)

#######################################################################

class MyFrame(wx.Frame):

    def __init__(self, size=(800,480)):
        wx.Frame.__init__(self, None, size=size)

        self.state = None
        self.panel = None

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)

        self.Show() # Show is used to show/hide window not to update content

        self.ChangePanel()

    #--------------------------

    def ChangePanel(self):

        print( "(debug) MyFrame.ChangePanel: state:", self.state)

        if self.state is None or self.state == 1:
            # change state
            self.state = 0

            # destroy old panel
            if self.panel:
                self.panel.Destroy()

            # create new panel
            self.panel = MyPanel(self, self.state, "C:/Users/Dimon/PycharmProjects/Game2/ball1.png", "C:/Users/Dimon/PycharmProjects/Game2/0.bmp")

            # add to sizer
            self.sizer.Add(self.panel, 1, wx.EXPAND)
        elif self.state == 0 :
            # change state
            self.state = 1

            # destroy old panel
            if self.panel:
                self.panel.Destroy()

            # create new panel
            self.panel = MyPanel(self, self.state, "C:/Users/Dimon/PycharmProjects/Game2/ball2.png", "C:/Users/Dimon/PycharmProjects/Game2/1.bmp")

            # add to sizer
            self.sizer.Add(self.panel, 1, wx.EXPAND)
        else:
            print( "unkown state:", self.state)

        self.Layout() # refresh window content

#######################################################################

class Application(wx.App):

    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)
        self.frame = MyFrame((800, 480))

    def run(self):
        self.MainLoop()

#######################################################################

if __name__ == "__main__":
    Application().run()