import wx
import order

class MyFrame(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,parent=superior,title='一个简单的订餐系统 by WSG',size=(480,600))
        
        #创建面板
        panel=wx.Panel(self)

        sizer=wx.GridBagSizer(5,5)

        self.customer=order.Customer('None')
        self.employee=order.Employee('0000')

        #标题
        maintitle=wx.StaticText(panel,label='一个简单的订餐系统')
        sizer.Add(maintitle,pos=(0,0),span=(0,3),flag=wx.TOP|wx.LEFT|wx.BOTTOM,border=15)
        font=wx.Font(18,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        maintitle.SetFont(font)
        maintitle.SetForegroundColour('blue')

        #图片
        img=wx.Image("icon.png",wx.BITMAP_TYPE_ANY)
        w=img.GetWidth()*0.25
        h=img.GetHeight()*0.25
        img.Rescale(w,h)
        imgicon=img.ConvertToBitmap()
        icon=wx.StaticBitmap(panel,bitmap=imgicon)
        sizer.Add(icon,pos=(0,4),flag=wx.EXPAND)

        #食物图标
        foodimg=[]
        for i in range(6):
            imgg=wx.Image("{n}.png".format(n=i+1),wx.BITMAP_TYPE_ANY)
            imgg.Rescale(30,30)
            imggg=imgg.ConvertToBitmap()
            foodimg.append(imggg)

        #加图标
        imgadd=wx.Image("add.png",wx.BITMAP_TYPE_ANY)
        imgadd.Rescale(20,20)
        imgaddicon=imgadd.ConvertToBitmap()

        #减图标
        imgsub=wx.Image("sub.png",wx.BITMAP_TYPE_ANY)
        imgsub.Rescale(20,20)
        imgsubicon=imgsub.ConvertToBitmap()


        #线
        line=wx.StaticLine(panel)
        sizer.Add(line,pos=(1,0),span=(1,5),flag=wx.EXPAND|wx.BOTTOM,border=10)

        #顾客姓名
        font1=wx.Font(12,wx.DEFAULT,wx.NORMAL,wx.NORMAL)
        text1=wx.StaticText(parent=panel,label='输入您的姓名：')
        text1.SetFont(font1)
        sizer.Add(text1,pos=(2,0),flag=wx.LEFT,border=10)
        self.input1=wx.TextCtrl(parent=panel) 
        sizer.Add(self.input1,pos=(2,1),span=(1,4),flag=wx.EXPAND|wx.RIGHT,border=10)
        
        #选择服务员
        text2=wx.StaticText(parent=panel,label='请选择服务员：')
        text2.SetFont(font1)
        sizer.Add(text2,pos=(3,0),flag=wx.LEFT|wx.TOP, border=10)
        self.empnum=['1000','1001','1002','1003']
        self.combo=wx.ComboBox(panel,value='请选择',choices=self.empnum)
        sizer.Add(self.combo,pos=(3,1),span=(1,4),flag=wx.TOP|wx.EXPAND|wx.RIGHT, border=10)
        
        #菜单复选框
        font2=wx.Font(15,wx.DEFAULT,wx.ITALIC,wx.NORMAL)
        title=wx.StaticBox(panel,label='今日菜单')
        title.SetFont(font2)
        title.SetForegroundColour('red')
        foodname=['可乐','汉堡','牛排','面条','包子','牛奶']
        foodprice=[12,14,34,23,23,11]
        self.menulen=len(foodname)
        self.foodlist=[]
        for i in range(self.menulen):
            food=order.Food(foodname[i],foodprice[i])
            self.foodlist.append(food)

        boxsizer=wx.StaticBoxSizer(title,wx.VERTICAL)
        self.menuCheckBox=[]
        self.CheckedFood=[]
        self.foodnumText=[]
        self.foodnumlist=[]
        self.addbuttonlist=[]
        self.subbuttonlist=[]
        
        for i in range(self.menulen):
            foodbox=wx.BoxSizer(wx.HORIZONTAL)
            img1=wx.StaticBitmap(panel,bitmap=foodimg[i]) #食物图片
            foodbox.Add(img1,flag=wx.ALL|wx.CENTER,border=5)

            checkbox=wx.CheckBox(panel,id=i,label=self.foodlist[i].showfd())
            checkbox.SetFont(font1)
            self.menuCheckBox.append(checkbox)
            self.CheckedFood.append(False)
            #self.Bind(wx.EVT_CHECKBOX,self.OnCheckBox,self.menuCheckBox[i])
            foodbox.Add(self.menuCheckBox[i],flag=wx.ALL|wx.CENTER,border=5) #食物名称

            subbutton=wx.BitmapButton(panel,id=i+100,bitmap=imgsubicon,style=10)
            self.subbuttonlist.append(subbutton)
            self.Bind(wx.EVT_BUTTON,self.OnSubButton,self.subbuttonlist[i])
            foodbox.Add(subbutton,flag=wx.LEFT|wx.CENTER,border=20) #减

            foodnum=wx.StaticText(panel,id=i,label="0")
            foodnum.SetFont(font2)
            self.foodnumText.append(foodnum)
            self.foodnumlist.append(0)
            foodbox.Add(foodnum,flag=wx.LEFT|wx.CENTER,border=10) #数量

            addbutton=wx.BitmapButton(panel,id=i+10,bitmap=imgaddicon)
            self.addbuttonlist.append(addbutton)
            self.Bind(wx.EVT_BUTTON,self.OnAddButton,self.addbuttonlist[i])
            foodbox.Add(addbutton,flag=wx.ALL|wx.CENTER,border=10) #加

            boxsizer.Add(foodbox,flag=wx.CENTER)

        sizer.Add(boxsizer,pos=(4,0),span=(1,5),flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT,border=10)
        
        font3=wx.Font(15,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        button1 = wx.Button(panel, size=(100,40),label='重置')
        button1.SetFont(font3)
        button1.SetForegroundColour('white')
        button1.SetBackgroundColour('slate blue')
        sizer.Add(button1, pos=(6, 0),flag=wx.LEFT, border=10)  
  
        button2 = wx.Button(panel, size=(100,40),label="下单")  
        button2.SetFont(font3)
        button2.SetForegroundColour('white')
        button2.SetBackgroundColour('slate blue')
        sizer.Add(button2, pos=(6, 3))  
  
        button3 = wx.Button(panel,size=(100,40), label="退出",style=0)
        button3.SetFont(font3)
        button3.SetForegroundColour('black')
        button3.SetBackgroundColour('white')
        sizer.Add(button3, pos=(6, 4), span=(1, 1), flag=wx.BOTTOM|wx.RIGHT, border=10) 
        
        sizer.AddGrowableCol(2)
        panel.SetSizer(sizer)

        #绑定事件
        self.Bind(wx.EVT_BUTTON,self.OnButtonReset,button1)
        self.Bind(wx.EVT_BUTTON,self.OnButtonCheck,button2)
        self.Bind(wx.EVT_BUTTON,self.OnButtonQuit,button3)
        
        
    def resizeBitmap(image,width=50,height=50):
        bmp=image.Scale(width,height).ConvertToBitmap()
        return bmp

    def OnButtonReset(self,event):#重置
        self.input1.Clear()
        self.combo.SetValue('请选择')
        for i in range(self.menulen):
            self.menuCheckBox[i].SetValue(False)
            self.foodnumText[i].SetLabel('0')
            self.foodnumlist[i]=0
        
    def OnButtonCheck(self,event):#确定
        try:
            cusname=self.input1.GetValue()
            empnum=self.combo.GetValue()
            flag=False
            for i in range(self.menulen):
                if not self.foodnumlist[i]==0:
                    flag=True
            if not cusname or empnum=='请选择' or flag==False:
                raise EOFError
            else:
                dlg=wx.MessageDialog(self,'确定下单？','注意',wx.CANCEL|wx.OK|wx.ICON_QUESTION)
                if dlg.ShowModal()==wx.ID_CANCEL:
                    return
        except EOFError:
            wx.MessageBox("信息填写不完整！",'注意',wx.OK|wx.ICON_EXCLAMATION)
            return
        self.customer.SetName(cusname)
        self.customer.delfoodordered()
        self.employee.SetNum(empnum)
        self.lunch=order.Lunch(self.customer,self.employee)
        for i in range(self.menulen):
            if not self.foodnumlist[i]==0:
                self.lunch.order(self.foodlist[i],self.foodnumlist[i])
        result=self.lunch.result()

        wx.MessageBox(result,'订餐结果',wx.OK|wx.ICON_EXCLAMATION)
        
    def OnCheckBox(self,event):
        cb=event.GetEventObject()
        self.CheckedFood[cb.GetId()]=cb.GetValue()

    def OnButtonQuit(self,event):#退出
        dlg=wx.MessageDialog(self,'确定退出订餐系统？','注意',wx.CANCEL|wx.OK|wx.ICON_QUESTION)
        if dlg.ShowModal()==wx.ID_OK:
            self.Destroy()
    
    def OnAddButton(self,event):#加
        ad=event.GetEventObject()
        fn=self.foodnumText[ad.GetId()-10]
        fn.SetLabel(str(int(fn.GetLabel())+1))
        self.foodnumlist[ad.GetId()-10]+=1

    def OnSubButton(self,event):#减
        sb=event.GetEventObject()
        fn=self.foodnumText[sb.GetId()-100]
        num=int(fn.GetLabel())
        if num==0:
            return
        fn.SetLabel(str(int(num-1)))
        self.foodnumlist[sb.GetId()-100]-=1

if __name__=='__main__':
    app=wx.App()
    frame=MyFrame(None)
    frame.Show()
    app.MainLoop()

