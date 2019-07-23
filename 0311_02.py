#循环语句，while,for,嵌套
#循环控制语句，break,continue

#continue
i=1
while i<10:
    i+=1
    if i%2>0:
        continue
    print(i)#可整除2的数值2,4,6,8,10

print('----continue------')

#break
i=1
while 1:
    print(i)
    i+=1
    if i>10:
        break
print("------break---------")

#for
for index in range(0,3): #range(3)
    print(index)

print('--------index--------')

index=0
star_names=['今冬','胡歌','刘涛']
for index in range(len(star_names)):
    print(star_names[index])
print('--name---')

#扩展，range
for i in range(1,5):
    print(i)
print('----range(1,5)-----')

for i in range(1,5,2):
    print(i)  #2表示步长
print('--range(1,5,2)--')

for i in range(5):
    print(i)
print('--range(5)---')

#嵌套循环
i=1
while(i<10):
    i=i+1
    while(i%6==0):
        print('老铁',i)
        break
    print('i--',i)

#迭代器 迭代器意思是能够一次返回它的一个成员（也就是里面的数值）
#栗子
list_lizi=[1,2,3,4]
it=iter(list_lizi) #iter是创建迭代器对象
# print(next(it)) #输出迭代器的第一个元素
# print(next(it)) #输出迭代器的第二个元素
# print(next(it)) #输出迭代器的第三个元素
# print(next(it)) #输出迭代器的第四个元素

#循环
try:
    while True:
        val=next(it)
        print(val)
except StopIteration:
    pass
print('---循环--try-expect---')

#列表

print("-----------------课上练习--------------------")
list_lx=['大本营','2019','笑傲江湖']
#追加值
list_lx.append('haha')
print('追加任意值--',list_lx)

#追加一个序列list
blist=[1,1,'222']
list_lx.extend(blist)
print('追加序列--',list_lx)

#在下标为1的元素前插入'charu'
list_lx.insert(1,'charu')
print('在下标为1的元素前插入''charu'':',list_lx)

#返回某元素下标
print('返回2019的下标：',list_lx.index('2019'))

#计算某元素出现次数
print('1出现的次数：',list_lx.count(1))

#删除某元素,del,remove,pop
del list_lx[1]
print('删除下表为ide元素charu后',list_lx)
list_lx.pop(2)#删除下标为2的元素
print('删除下标为2的元素',list_lx)
list_lx.remove('2019')#删除2019
print('删除2019',list_lx)

print('\n---------------排序---------------------\n')
#对list_sort=[2,3,1,4]进行正向，反向，排序
list_sort=[2,3,1,4]
print('原列表',list_lx)

list_sort.reverse()
print("反向",list_sort)#反向,操作元素反向展示

#sort非同种元素报错
list_sort.sort() #默认升序展示
print('默认升序展示',list_sort)
list_sort.sort(reverse=True)#降序展示
print('降序展示',list_sort)

print('\n----------------元组--------------------\n')

#元组

#del可散户整个元组，不能删除单个元素，元组元素不允许修改

tup=