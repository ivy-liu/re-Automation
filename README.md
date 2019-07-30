
* 私有变量和方法
---

__private_attrs:两个下划线开头，生命该属性为私有，不能在类的外部被使用或直接访问。


在类内部的方法中使用：self.__private_attrs

个人觉得python的私有没有什么意义，规则存在，
但实际通过对象调用类，调用私有方法依然可以使用
```python
class Animal:
    def __heshui(self):
        print('动物，喝水')

    def test_heshui(self):
        self.__heshui()#调用类内部私有方法：self.__heshui()需要使用self

class Cat(Animal):
    def heshui(self):
        super()._Animal__heshui()
    # def cat_heshui(self):
    #     pass
new_cat=Cat()
# new_cat.__heshui()#报错 外部无法访问

new_cat.heshui()#运行正常，打印：动物，喝水

```
* testlink+vertrigo
---
windows下安装testlink，进入安装页面后，在检查一些相关配置环境时报错，如下：  

Checking if /var/testlink/logs/ directory exists [S] </B<< td> Failed!  
Checking if /var/testlink/upload_area/ directory exists [S] </B<< td> Failed!  


解决办法：  
修改testlink下的config.inc.php文件：  
注释：$tlCfg->log_path = '/var/testlink/logs/'; /* unix example   
添加：$tlCfg->log_path = '[testlinkDir]/logs/';  

注释：$g_repositoryPath = '/var/testlink/upload_area/'; /* unix example   
添加：$g_repositoryPath = '[testlinkDir]/upload_area/';  
注意：[testlinkDir] 表示安装目录路径，如：D:\xampp\htdocs\testlink，  

改‘\’为‘/’  
 
修改后保存，刷新页面。  



其他补充  
1.Testlink安装完成，可使用以下地址访问  
http://localhost/testlink-1.9.19/login.php  
访问的账号密码为admin/admin  

2.若需要管理mysql数据库，访问地址为  
http://localhost  
http://localhost/phpmyadmin/index.php  
访问的账号密码为root/vertrigo  

3.Testlink汉化，不同账号可以单独设置。  
登录Testlink，mysettings>Personal data>locale>Chinese Simplified，设置后save保存。  



* 数据库插入数据
---
```python
# 元组插入
print('----元组插入---')
# 此处%s为占位符，不是格式化字符串，所以age用%s
stu_info_tup = '''
insert into student(StdName,Gender,Age)values(%s,%s,%s)
'''
data = ('小强', 'M', 21)
cursor.execute(stu_info_tup, data)

# 提交操作，不提交不生效，2选1
con.commit()
# cursor.execute('commit')

cursor.close()  # 关闭游标
con.close()  # 关闭连接

# 1.连接数据库
# 2.创建游标
# 3.执行cursor.execute(stu_info)，‘stu_info’SQL语句
# 4.cursor.close()  # 关闭游标  con.close()  # 关闭连接

```



  