import wx
import gui


class GuiFrameMain(gui.FrameMain):
    def __init__(self, parent):
        gui.FrameMain.__init__(self, parent)
        self.SetIcon(wx.Icon("resource/icon-app.ico"))

    def btnTest(self, event):
        wx.MessageBox("Hello, World!", "MyApp", wx.OK | wx.ICON_INFORMATION)
        event.Skip(False)

    def cmbChanged( self, event ):
        wx.MessageBox("Hello, World! COMBO box changed", "MyApp", wx.OK | wx.ICON_INFORMATION)
        event.Skip(False)


if __name__ == '__main__':
    app = wx.App(False)
    app.SetAppName("MyApp")

    frame = GuiFrameMain(None)
    frame.Show(True)
    app.MainLoop()
