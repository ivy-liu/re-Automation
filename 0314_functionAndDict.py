#函数、字典


#字典中的操作
print('取值\n')
dict1={'name':'小强','age':18,'class':'first'}
print("dict1['name'] 名字为",dict1['name'])
print("dict1.get('name') 名字为",dict1.get('name'))
print(dict1.get(18))

#修改
print("\n修改\n")
print('原字典',dict1)
dict1['name']='花花'
print('现字典',dict1)

#新增
print("\n新增\n")
dict1['school']='啥啥大学'
print('新增school后字典',dict1)

#删除
print("\n删除\n")
del dict1['school']
print('删除school后字典',dict1)

dict1.clear()
print('清空字典后',dict1)
# del dict1
# print('删除字典后',dict1)#报错

'''
字典要点
1，键不允许相同，如果相同，后面的值覆盖前面的值
2，键是不可变的，所以只能用数字、字符串、元组来担当
'''
print()
dict2={(1,2):'元组',1:10,'aa11':11}
print(dict2)
print(dict2[(1,2)])

print(dict2[1])
print(dict2['aa11'])


#练习 分别实现一次性输出所有keys,或者所有values
dict3={'name':'小强','age':18,'class':'first'}
print(dict3.keys())
print(dict3.values())
print(dict3.items())
print()

#遍历字典
for key, value in dict3.items():
    print (key, ':', value)
#1.遍历键、值
list_key=[]
list_value=[]
for key in dict3:

    list_key.append(key)
    list_value.append(dict3[key])

    print('keys',list_key)
    print('values',list_value)
print()
#2.遍历键、值
for key in dict3.keys():
    print('key为',key)
for value in dict3.values():
    print('value为',value)
print()

#函数
import unittest
class MyTest(unittest.TestCase):
    def print_me_test(str01,str02):
        print('str01-',str01)
        print('str02-',str02)
        print('完毕')
    def test_test():
        print_me_test('sssss','222222222')
#pyton内值引用传递，要变都变

print("---------函数花式传值-----------")

#age=22是默认值，未传值时使用
def print_info(name,age=22):
    print(('姓名：%s,年龄：%d')%(name,age))
    return

print_info(name='小强',age=18) #姓名：小强,年龄：18
print_info(age=44,name='小花') #姓名：小花,年龄：44
print_info(name='明明') #姓名：明明,年龄：22

print('\n------不定长参数---------\n')
def print_info(arg1,*var):
    print('输出：',arg1)
    for v in var:
        print(v)
    return
print_info(10)
print()
print_info(70,60,50)

print('----匿名函数lambda----')
'''
1.lambda只是一个表达式，而不是一个代码块，函数体比def简单很多，
仅仅能在lambda表达式中封装有限的逻辑进去。
2.语法：
lambda[arg1][arg2][]...:expression
'''

sum=lambda arg1,arg2:arg1+arg2
#调用
print('相加后的值为:',sum(10,20))

#全局变量、局部变量
'''
1.定义在函数内部的变量，拥有局部作用域，定义在函数外的拥有全局作用域
2.局部变量只能在被声明的函数内访问，全局变量可以整个程序使用
'''
#global关键字
counter=1
def doing():
    global counter
    for i in (1,2,3):
        counter+=1
doing()
print('counter-',counter) #counter- 4

print()
#练习
print('--练习--')
x='xiaoqiang'
def func():
    x='a'
    def func2():
        print('x=',x) #x= a
    func2()
func()
print(x)


#range
print('-------range-------\n')
range(4)
range(0,4)
range(0,4,1)
#0,1,2,3

range(1,4,-1)
for i in range(1,4,-1):
    print('range(1,4,-1):',i)
    #无值,空
range(-3,3)
for i in range(-3,3):
    print('range(-3,3)',i)#-3,-2,-1,0,1,2

print()
range(3,-3,1)
for i in range(3,-3,-1):
    print('range(3,-3,-1)',i)#3,2,1,0,-1,-2

print()

#切片
#a,b,c,d
string='abcd'
print(string[-1:-5:-1]) #dcba



