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