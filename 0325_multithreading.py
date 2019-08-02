import threading
import time

#要运行的任务，函数形式
def music():
    time.sleep(5)
    print('音乐')

#要运行的任务，函数形式
def book(name):
    time.sleep(5)
    print(name)

#创建线程，注意语法格式。target为目标函数，args为传递的参数（可选）
t1=threading.Thread(target=music)
t2=threading.Thread(target=book,args=('小萌',))
#启动线程
t1.start()
t2.start()
print('抢地主')


print('\n---------------继承类形式--------------------\n')
#类形式
class myThread(threading.Thread):
    #可选的类方法
    def __init__(self,name):
        threading.Thread.__init__(self)#固定格式
        self.name=name
    #重写run方法
    #不能确定run()再不同线程执行顺序，这个由CPU决定
    def run(self):
        #调用函数book_class，并传递参数name
        book_class(self.name)
#函数
def book_class(name):
    time.sleep(5)
    print(name)
#创建线程
mt1=myThread('小妹喜欢斗地主')
mt2=myThread('不抢！')
#启动线程，每个线程对象必须调用一次该函数，它会自动调用run方法
mt1.start()
mt2.start()
print('等的花都谢了--')