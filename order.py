class Customer:                 #顾客类
    def __init__(self,cusname):
        self.__cusname=cusname
        self.__foodordered=[]
       # print("您成功创建一个顾客身份:{name}".format(name=self.__cusname).center(50,'='))
    
    def SetName(self,cusname):
        self.__cusname=cusname
    
    def ShowName(self):
        return self.__cusname

    def placeOrder(self,emp,food,num):   #顾客点餐
        self.__emp=emp
        self.__foodordered.append(self.__emp.takeOrder(food,num))

    def delfoodordered(self):
        self.__foodordered.clear()

    def printMenu(self):        #打印顾客菜单
        result=''
        self.__foodpricesum=0
        result=(" {num} 号服务员已为 {name} 成功点餐".format(num=self.__emp._Employee__empnum,name=self.__cusname).center(30,'='))
        for i in range(len(self.__foodordered)):
            fd=self.__foodordered[i][0]
            fdnum=self.__foodordered[i][1]
            result+="\n{:18}. {food}  ×{n}".format(i+1,food=fd.showfd(),n=fdnum)
            self.__foodpricesum+=fd.showfdprice()*fdnum
        result+="\n\n"
        result+="合计：{sum} 元".format(sum=str(self.__foodpricesum)).rjust(50)
        return result

class Employee:                 #服务员类
    def __init__(self,empnum):
        self.__empnum=empnum
        #print("已成功为您叫到 {num} 号服务员".format(num=empnum).center(50,'='))

    def SetNum(self,empnum):
        self.__empnum=empnum

    def takeOrder(self,food,num):        #服务员记录顾客点的菜单
        return [food,num]


class Food:                     #食物类
    def __init__(self,foodname,price):
        self.__foodname=foodname
        self.__price=price

    def showfdname(self):     
        return self.__foodname

    def showfdprice(self):
        return self.__price

    def showfd(self):
        return self.__foodname+'---'+str(self.__price)+'元'

class Lunch:
    def __init__(self,cus,emp):
        self.__Cus=cus
        self.__Emp=emp
        #print("您现在可以点餐了".center(50,'='))

    def order(self,food,num):
        self.__Cus.placeOrder(self.__Emp,food,num)

    def result(self):
        return self.__Cus.printMenu()

if __name__=='__main__':
    print("Please use me as a module.")
    print("一个简单的订餐系统".center(50,'='))
    while True:
        try:
            cusname=input("请输入顾客姓名：")
            if not cusname:
                raise EOFError
            break
        except EOFError:
            print("您未输入任何内容，请重新输入".center(50,'*'))
    cus1=Customer(cusname)

    while True:
        try:
            empnum=(input("您需要几号服务员为您服务："))
            break;
        except ValueError:
            print("您输入了非法字符，请重新输入".center(50,'*'))
    emp1=Employee(empnum)

    lun1=Lunch(cus1,emp1)
    lun1.order()
    lun1.result()

