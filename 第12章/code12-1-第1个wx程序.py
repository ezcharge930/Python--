import wx


def onClick(event):
    print('按钮被点击了')
    
    
    
    
# 创建应用程序对象
app = wx.App()

# 创建窗口
# size：宽，高 pos:x坐标，y坐标
frm = wx.Frame(None,title='mia学习系统',size=(1000,400),pos=(600,300))

# 显示窗口
frm.Show()

# 创建面板
pl = wx.Panel(frm,size=(500,500),pos=(80,100))

# 显示面板
pl.Show()

# 创建静态文本
staticText = wx.StaticText(pl,label = '欢迎学习python',pos=(100,100))

# 显示静态文本
staticText.Show()

# 创建按钮
btn = wx.Button(pl,label = '测试')

# 显示按钮
btn.Show()

# 给按钮绑定时间
frm.Bind(wx.EVT_BUTTON,onClick,btn)



# 进入主循环，让窗口一直显示
app.MainLoop()