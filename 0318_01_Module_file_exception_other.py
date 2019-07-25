#2018-3-18上午模块文件异常其他
'''
'r'：打开只读文件，该文件必须存在
'w'：打开只写文件，若文件存在则文件长度清为0，即该文件内容会消失。若文件不存在则建立该文件
'a'：以附加的方式打开只写文件。若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留
'r+' ： r+w（可读可写，文件若不存在就报错(IOError)）
'w+' ： w+r（可读可写，若文件存在则文件长度清为零，即该文件内容会消失。若文件不存在则建立该文件）
'a+' ： a+r（可追加可写，若文件不存在，则会建立该文件，如果文件存在，写入的数据会被加到文件尾后，即文件原先的内容会被保留）
'''

def bubble_sort(nums):
    for i in range(len(nums) - 1):  # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums) - i - 1):  # j为列表下标
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
 
print(bubble_sort([45, 32, 8, 33, 12, 22, 19, 97]))
# 输出：[8, 12, 19, 22, 32, 33, 45, 97]


print('\n---from 文件名---')
import sum
print(sum.add_two_num(1,2))

print('\n---from 文件名 import 函数/类----')
from sum import add_two_num
print(add_two_num(2,2))

print('\n---from 文件名 import 文件名----')
from test_folder import test_sum
print(test_sum.test_add_two_num(2,3))


# from...import *
print()

#文件读取

#两个\\
doc_path='D:\\python_code\\re_Automation\\test.txt'#绝对路径
print('-open-')
file_open=open(doc_path,'r')
print('文件名是：',file_open.name)
print('是否关闭了文件',file_open.closed)#是否关闭了文件 False
print('打开方式',file_open.mode)

file_open.close()
print('是否关闭了文件',file_open.closed)#是否关闭了文件 True
print()


#相对路径
doc_write='.\\test.txt'
#打开文件夹
fo=open(doc_write,'w+',encoding='utf-8')#未加上encoding='utf-8'时，查看写入的内容是乱码
fo.write('大家好，我是lvy')
print('打开方式',fo.mode)

str1=fo.read()
print('1.文件内容是--',str1)

print(fo.tell()) #打印文件内当前位置
print(fo.seek(0))#位置移动到最前
print(fo.tell())

str1=fo.read()
print('2.文件内容是str1--',str1)

str2=fo.readlines()
print('文件内容是str2--',str2)
#关闭文件
fo.close()

