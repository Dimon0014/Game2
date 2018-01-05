#!/usr/bin/env python

import wx
import images

#import wx.lib.buttons
#wx.BitmapButton = wx.lib.buttons.GenBitmapButton

#----------------------------------------------------------------------

class TestPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1,
                         style=wx.NO_FULL_REPAINT_ON_RESIZE)
        self.log = ""

        if 0:  # a test case for catching wx.PyAssertionError

            #wx.GetApp().SetAssertMode(wx.PYAPP_ASSERT_SUPPRESS)
            #wx.GetApp().SetAssertMode(wx.PYAPP_ASSERT_EXCEPTION)
            #wx.GetApp().SetAssertMode(wx.PYAPP_ASSERT_DIALOG)
            #wx.GetApp().SetAssertMode(wx.PYAPP_ASSERT_EXCEPTION | wx.PYAPP_ASSERT_DIALOG)

            try:
                bmp = wx.Bitmap("C:/Users/Dimon/PycharmProjects/Game2/8.bmp", wx.BITMAP_TYPE_BMP)
                mask = wx.Mask(bmp, wx.BLUE)
            except wx.PyAssertionError:
                self.log.write("Caught wx.PyAssertionError!  I will fix the problem.\n")
                bmp = images.Test2.GetBitmap()
                mask = wx.MaskColour(bmp, wx.BLUE)
        else:
            bmp = images.Test2.GetBitmap()
            mask = wx.Mask(bmp, wx.BLUE)

        bmp.SetMask(mask)
        b = wx.BitmapButton(self, -1, bmp, (20, 20),
                       (bmp.GetWidth()+10, bmp.GetHeight()+10))
        b.SetToolTip("This is a bitmap button.")
        self.Bind(wx.EVT_BUTTON, self.OnClick, b)

        b = wx.BitmapButton(self, -1, bmp, (20, 120),
                            style = wx.NO_BORDER)

        # hide a little surprise in the button...
        img = images.Robin.GetImage()
        # we need to make it be the same size as the primary image, so
        # grab a subsection of this new image
        cropped = img.GetSubImage((20, 20, bmp.GetWidth(), bmp.GetHeight()))
        b.SetBitmapPressed(cropped.ConvertToBitmap())

        b.SetToolTip("This is a bitmap button with \nwx.NO_BORDER style.")
        self.Bind(wx.EVT_BUTTON, self.OnClick, b)


    def OnClick(self, event):
        self.log.write("Click! (%d)\n" % event.GetId())


#----------------------------------------------------------------------

# def runTest(frame, nb, log):
#     win = TestPanel(nb, log)
#     return win

#----------------------------------------------------------------------


overview = """<html><body>
<h2>BitmapButton</h2>

<p>A BitmapButton control displays a bitmap. It can have a separate bitmap for each button state: normal, selected, disabled.</p>

<p>The bitmaps to be displayed should have a small number of colours, such as 16,
to avoid palette problems.</p>

<p>A bitmap can be derived from most image formats using the wx.Image class.</p>

</body></html>
"""

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Simple Notebook Example")

        # Here we create a panel and a notebook on the panel
        p = TestPanel(self) # типа парент self - короче сам себе парент
        # nb = wx.Notebook(p)
        #
        # # create the page windows as children of the notebook
        # page1 = PageOne(nb)
        # page2 = PageTwo(nb)
        # page3 = PageThree(nb)
        #
        # # add the pages to the notebook with the label to show on the tab
        # nb.AddPage(page1, "Page 1")
        # nb.AddPage(page2, "Page 2")
        # nb.AddPage(page3, "Page 3")

        # finally, put the notebook in a sizer for the panel to manage
        # the layout
        sizer = wx.BoxSizer()
        # sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()

