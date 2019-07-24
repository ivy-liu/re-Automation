#函数、字典


#字典中的操作
print('取值\n')
dict1={'name':'小强','age':18,'class':'first'}
print("dicta['name'] 名字为",dict1['name'])
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
