import threading
import time

#要运行的任务，函数形式
def music():
    time.sleep(5)
    print('t1-音乐')

#要运行的任务，函数形式
def book(name):
    time.sleep(5)
    print('输出：',name)

#创建线程，注意语法格式。target为目标函数，args为传递的参数（可选）
#可传：('t2-小萌',)、args=(i,)i为数组，遍历执行、args=['t4-小小萌',]、args=(m,)把数组当作1个参数
t1=threading.Thread(target=music)
t2=threading.Thread(target=book,args=('t2-小萌',))#注意这个逗号 输出： t2-小萌
m1=['t3-小萌1','t3-小萌2','t3-小萌3',]
for i in m1:
    t3=threading.Thread(target=book,args=(i,))
    t3.start()
    #输出： t3-小萌2
    #输出： t3-小萌3
    #输出： t3-小萌1
t4=threading.Thread(target=book,args=['t4-小小萌',])#输出： t4-小小萌
m=[1,2,3,4,5,'t5']
t5=threading.Thread(target=book,args=(m,))#输出： [1, 2, 3, 4, 5]

#启动线程
t1.start()
t2.start()
t4.start()
t5.start()
print('抢地主')


print('\n---------------继承类形式--------------------\n')
#类形式
class myThread(threading.Thread):
    #可选的类方法
    def __init__(self,name):
        threading.Thread.__init__(self)#固定格式
        self.name=name
    #重写run方法
    #不能确定run()再不同线程建立间 执行顺序，这个由CPU决定
    def run(self):
        #获得锁，成功获得锁定后返回true,可选的timeout参数不填时将一直堵塞知道获得锁定的任务完成
        threadLock.acquire()
        #调用函数book_class，并传递参数name
        book_class(self.name)
        #释放锁，开始下一个线程
        threadLock.release()

#函数
def book_class(name):
    time.sleep(5)
    print(name)

threadLock=threading.Lock()

#创建线程
mt1=myThread('抢地主!')
mt2=myThread('不抢！')
#启动线程，每个线程对象必须调用一次该函数，它会自动调用run方法
mt1.start()
mt2.start()

mt1.join(timeout=50)
mt2.join()#存在join后'等的花都谢了--'一定是最后执行
print('等的花都谢了--')


#锁
'''
join():阻塞线程，直到该线程执行完毕，才会运行后面的代码
threading.Lock():如果使用RLock，那么acquire和release必须成对出现，
  即调用了n次acquire，必须调用n次的release才能真正释放所占用的锁
threading.RLock():多重锁RLock允许在同一线程中被多次acquire。而Lock却不允许这种情况。

好处：确保了某段关键代码只能由⼀个线程从头到尾完整地执⾏
坏处：由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对⽅持有的锁时，可能会造成死锁。
'''



#生产者、消费者
'''
全局变量x
生产者：x>0 wait(print) 否则x+1(for)
消费者：x+0 wait print 否则x-1 for
生产者和消费之分别是一个class
'''
import random
import threading
x=0
class Producer(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)#固定格式
        self.name=name
    def run(self):
        global x
        if x>0:
            print('存在库存，不再生产')
        else:
            # i=random.randint(1,10)
            for i in range(5):
                x=x+i
                print('Producer-%s-现有库存：%d'%(self.name,x))
class Consumer(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)#固定格式
        self.name=name
    def run(self):
        global x
        if x>0:  
            for i in range(5):
                x=x-1
                print('Consumer-%s-现有库存：%d'%(self.name,x))
        else:
            print('没有库存，不再消耗')

p=Producer('小明')
p.start()
# p.join()
c=Consumer('红红')
c.start()
# c.join()




            