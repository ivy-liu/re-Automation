#静态方法
@staticmethod
def func1():
    print('我是静态函数，参数可以为空')
#可以类名调用静态方法，可以对象调用

#定义一个员工类
# 在创建类的对象时，要求进行对员工的姓名、工作初始化
# 类中有2个一般方法，一个打印员工数量（创建的对象数），一个打印员工信息（姓名、工资）
class MyClass:
    staff_count=0
    def __init__(self,name,wage):
        self.name=name 
        self.wage=wage
        MyClass.staff_count+=1
    def printInfomation(self):    
        print('员工信息：',self.name,self.wage)
    def printCount(self):
        print('员工数量：',MyClass.staff_count)

aStaff=MyClass('张三','10k')
aStaff.printInfomation()
aStaff.printCount()

bStaff=MyClass('李四',8000)
bStaff.printInfomation()
bStaff.printCount()

print()
#实现一个shape类，用getarea方法计算面积，用getlong方法计算周长
import math  #math.pi 
class Shape:
    def getArea(self,r):
        area=r**2*math.pi
        print('半径%d的圆，面积为%.2f' % (r,area))
        return area
    def getLong(self,r):
        long=r*2*math.pi
        print('半径%d的圆，周长为%.2f' % (r,long))
        return long
a=Shape()
a.getArea(3)
a.getLong(2)

print('\n------------------类的继承---------------------\n')
#类的继承
'''
Class Student(User):
1.子类可以继承或重写父类的方法
2.子类可以自定义新的方法或成员变量

'''

class Parent:
    r=5
    def getArea(self):
        area=r**2*math.pi
        print('父类-半径%d的圆，面积为%.2f' % (r,area))
        return area
    def printParent(self):
        print('\n来自父类\n')
#继承父类
class Child(Parent):
    v=3
    #重写父类方法
    def getArea(self,r):
        area=r**2*math.pi
        print('子类-半径%d的圆，面积为%.2f' % (r,area))
        return area
    def printChild(self):
        print('\n来自子类\n')
xiaoming=Child()
xiaoming.printParent()
xiaoming.printChild()
print('拿到父类的属性-r：',xiaoming.r)
print('拿到子类的属性-v：',xiaoming.v)
#重写父类方法调用
xiaoming.getArea(3)
# xiaoming.getArea()#报错 缺少参数r

print('\n-------------私有变量和方法----------------\n')

#私有变量和方法
#__private_attrs:两个下划线开头，生命该属性为私有，不能在类的外部被使用或直接访问。
# 在类内部的方法中使用：self.__private_attrs

#个人觉得python的私有没有什么意义，规则存在，
# 但实际通过对象调用类，调用私有方法依然可以使用

class Animal:
    def __heshui(self):
        print('动物，喝水')

    def test_heshui(self):
        self.__heshui()#调用类内部私有方法：self.__heshui()需要使用self

class Cat(Animal):
    def heshui(self):
        super()._Animal__heshui()
    # def cat_heshui(self):
    #     pass
new_cat=Cat()
# new_cat.__heshui()#报错 外部无法访问

new_cat.heshui()#运行正常，打印：动物，喝水

