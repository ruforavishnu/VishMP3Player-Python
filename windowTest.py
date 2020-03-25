class ShapedFrame(wx.Frame):

wx.Frame._init_(self, None, -1, style = wx.FRAME_SHAPED | wx.FRAME_NO_TASKBAR) self.hasShape = False self.bmp = images.getVippiBitmap() self.SetClientSize((self.bmp.GetWidth() dc = wx.ClientDC(self) dc.DrawBitmap(self.bmp, 0,0, True) self.SetWindowShape() self.Bind(wx.EVT_LEFT_DCLICK, self.OnDoubleClick) self.Bind(wx.EVT_RIGHT_UP, self.OnExit) self.Bind(wx.EVT_PAINT, self.OnPaint)

self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)

Acquiring the image ho self.bmp.GetHeight()))

Drawing the image

def SetWindowShape(self, evt=None): r = wx.RegionFromBitmap(self.bmp) self.hasShape = self.SetShape(r)

def OnDoubleClick(self, evt): if self.hasShape:

Setting the shape d

Binding the window create event self.SetShape(wx.Region()) <1—i „ ...

self_hasShape = False © the'shlpe else:

self.SetWindowShape()

def OnPaint(self, evt): dc = wx.PaintDC(self) dc.DrawBitmap(self.bmp, 0,0, True)

def OnExit(self, evt): self.Close()

if __name__ == '__main__': app = wx.PySimpleApp() ShapedFrame().Show() app.MainLoop()