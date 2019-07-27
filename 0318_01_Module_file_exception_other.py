#2018-3-18上午模块文件异常其他
'''
'r'：打开只读文件，该文件必须存在
'w'：打开只写文件，若文件存在则文件长度清为0，即该文件内容会消失。
     若文件不存在则建立该文件
'a'：以附加的方式打开只写文件。
     若文件不存在，则会建立该文件，
     如果文件存在，写入的数据会被加到文件尾，即文件原先的内容会被保留
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
fo.write('你好，lvy')
print('打开方式',fo.mode)

str1=fo.read()
print('1.文件内容是--',str1)

print('当前位置-',fo.tell()) #打印文件内当前位置

print(fo.seek(0,0))#位置移动到最前
print('当前位置0-',fo.tell())

print(fo.seek(9))#位置移动到'你好，'后
print('当前位置9-',fo.tell())

str1=fo.read()
print('2.文件内容是str1--',str1)

str2=fo.readlines()
print('文件内容是str2--',str2)

#关闭文件
fo.close()

'''
seek() 方法用于移动文件读取指针到指定位置。

1.fileObject.tell()方法告诉文件当前的位置
2.fileObject.seek(offset[,whence])方法改变当前位置
offset -- 开始的偏移量，也就是代表需要移动偏移的字节数
whence：可选，默认值为 0。
给offset参数一个定义，表示要从哪个位置开始偏移；
0代表从文件开头开始算起，
1代表从当前位置开始算起，
2代表从文件末尾算起。
'''

#以w方式打开某个文件，通过write和writelines分别写入内容
new_path='.\\new_file.txt'
new_file=open(new_path,'w',encoding='utf-8')
new_file.write('你好，此时write写入\n')

new_file.writelines(['小明\n','小兰\n','小花\n'])#可字符串、可列表


# print('尝试')
# new_file.write(['小明\n','小兰\n','小花\n'])#must be str, not list
new_file.close()

#以w+方式打开文件，写两行数据，部关闭文件，继续读取文件全部内容
new_path_01='.\\new_file_01.txt'
new_file_01=open(new_path_01,'w+',encoding='utf-8')
new_file_01.writelines(['ivy,哈哈哈,哈哈哈哈\n','ivy,呵呵呵,呵呵呵呵,呵呵呵'])
new_file_01.seek(0)
print('打印new_file_01:\n',new_file_01.readline())
print('打印下一行：\n',new_file_01.readline())
new_file_01.close() 

print()


print('-------------异常处理----------\n')

log_path='.\\file.txt'

# try:
#     fh=open(log_path,'r')
#     fh.write('尝试写入')
# except IOError as e:
#     print('该文件不存在，且只读权限，写入失败',str(e))
#     # fh.close()
# else:#try没有异常时执行else
#     print('写入成功')
#     # fh.close()


# try:
#     fh01=open(log_path,'r')
#     fh01.write('尝试写入')    
# finally:#无论try是否成功都要执行
#     print('该文件不存在，且只读权限，写入失败，执行finall')
    

'''
random,glob
'''
print('\n-----随机数----------')
import random
print('拿到一个随机值-',random.choice('abcdefghijklmn'))#随机取这些字母
print('从列表中随机取值-',random.choice(['apple','pear','banana']))

import glob
print('\n-----glob----------')
print(glob.glob('*.txt'))#['new_file.txt', 'new_file_01.txt', 'test.txt']
#根据指定通配符去匹配
# print(glob.glob('D:\\P*'))

import os
print('\n---------和os接口交互---------')
print('当前目录：',os.getcwd())
#打印制定目录下所有的文件名（带路径）。统一用 c:\Program Files
# 提示：os.listdir，join
#os.listdir(path)
# 返回指定路径下的文件和文件夹列表。
# path='.\\'
path=os.getcwd()
dirs=os.listdir(path)
#输出所有文件和文件夹
for i in dirs:
     re_path=os.path.join(path,i)
     print(re_path)
print()
print('\n----递归显示目录，目录下文件---')

def readFiles(path):
     dirs=os.listdir(path)
     for i in dirs:
          re_path=os.path.join(path,i)
          
          if os.path.isfile(re_path):#isfile判断是不是文件  isdir判断是不是目录 入参都需要绝对路径
               print(re_path)
          else:
               readFiles(re_path)
          
print()
print('---------执行递归函数---------')
readFiles(os.getcwd())