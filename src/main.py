import wx
import gui


class GuiFrameMain(gui.FrameMain):
    def __init__(self, parent):
        gui.FrameMain.__init__(self, parent)
        self.SetIcon(wx.Icon("resource/icon-app.ico"))

    def btnTest(self, event):
        wx.MessageBox("Hello, World!", "MyApp", wx.OK | wx.ICON_INFORMATION)
        event.Skip(False)


if __name__ == '__main__':
    app = wx.App(False)
    app.SetAppName("MyApp")

    gui_frame_main = GuiFrameMain(None)
    gui_frame_main.Show(True)
    app.MainLoop()
