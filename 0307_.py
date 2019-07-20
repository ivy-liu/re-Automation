list1=['abcd',789,'xiaoqiang',70.1]
print(list1)
print(list1[0])
print(list1[0][0])
# 0715
list1[1]=123
print(list1)
#列表是有序的对象，字典是无序的对象
dict={'name':'小强测试品牌','code':'g6755'}
print(dict.get('name','not found'))
#有就打印，没有就打印后面的

a=100
print('小强得分为：'+str(a))

h='175'
print('小强的身高为：',int(h))

l="1000"
print('长度为：',len(l))
#len字符串长度，列表个数
print('列表长度',len(list1))

#输出
w=10
print(w)
print('w=',w)
print()

var='holle beijing'
print('更新追加字符串',var[:6]+'xiaoming\n')

#字符串格式化输出
print('我是%s年龄%d'%('小强',18))
#顺序对应

#格式化输出
a=10
print('a-%.2f' % a)#2位小数
print('a-%.1f' % (a*3))#1位小数

