#算术运算符
a=21
b=10
c=0

c=a+b
print("a+b=",c)

c=a//b
print("a//b=",c)#取整除 - 返回商的整数部分（向下取整）

c=a/b
print("a/b=",c)

c=a**b
print("a**b=",c)

c=a*b
print("a*b=",c)

#条件语句，判断
jin=90
qu=75
ts=(jin-qu)/qu*100
print('小明成绩提升百分点：%.1f' % ts+'%')

flag=False
name="xiaoming"
if name=='小明'or'xiaoming':
    flag=True
    print('是的，对，我是小明')
else:
    print('不是')


num=5
if num==3:
    print('我是3')
elif num==4:
    print('我是4')

else:
    print('我好困，我是5')


num=9
if num >=0 and num <=10:
    print('我大于等于0小于等于10\n')

height=1.68
weight=53
bmi=weight/(height**2) #体重除以身高的平方

print('bmi=',bmi)
if bmi<18.5:
    print('过轻')
elif bmi>=18.5 and bmi <=25:
    print('正常')
elif bmi>25 and bmi<=28:
    print('过重')
elif bmi>28 and bmi <=32:
    print('肥胖')
elif bmi>32:
    print('严重肥胖')
else:
    print('异常')

