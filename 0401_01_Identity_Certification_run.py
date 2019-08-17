#基本身份认证（“用户名：密码”采用 Base-64 编码）
import requests 
from requests.auth import HTTPBasicAuth 
auth=HTTPBasicAuth(username,password) 
requests.post(url,auth=auth)

#摘要式身份认证（密码是MD5 加密）
import requests
from requests.auth import HTTPDigestAuth 
auth=HTTPDigestAuth(username,password) 
requests.get(url, auth=auth)

# SSL 证书验证
import requests 
#下面这个适用于服务器端证书 
requests.get(url,verify=True)#false 为关闭验证，可以不去验证 
#下面这个适用于客户端证书 
requests.get(url, cert=('/path/server.crt')) 
# PS：console 里可能会有一些warning 的提示，可以不用管 ta，
# 如果看的不舒服，可以 通过下面的语句屏蔽： 
from requests.packages.urllib3.exceptions import InsecureRequestWarning 
# 禁用安全请求警告 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# session 用法
session=requests.Session()#初始化一个 session 对象 
session.get(url)#用户信息 cookies 保存在 session 中

#运行
import unittest #封装好的单元测试框架，可以直接使用 
class TestAdd(unittest.TestCase): #编写的测试类中需要继承 unittest.TestCase 
    #可选，在每个测试方法执行前调用，用于设置初始化的部分 
    def setUp(self): print("我是 setUp")
#可选，在每个测试方法执行后调用，这个地方做所有测试用例执行完成的清理工作 
def tearDown(self): 
    print("我是 teardown")
#测试 case，一定是以 test 开头啊 
def test_01_add(self): 
    a=1 
    b=2 
    c=a+b

    #断言判断 
    self.assertEqual(c,3,msg='实际结果不符合预期') 
    print('c=',c," 实际结果符合预期\n")
#运行的几种方式，根据实际情况选择一种运行即可 
# #1、一次全部运行 
unittest.main() 
# #2、TestSuite 测试套件：可自由组合测试 case，常用的方法是 addTest

''' 
suite = unittest.TestSuite() 
suite.addTest(TestAdd("test_01_add")) #添加测试用例方法名,测试类名-方法名 
#TextTestRunner 测试执行，就是来执行我们的脚本，常用方法是 run 
#自动找 test 开头的进行运行 
runner = unittest.TextTestRunner(verbosity=2) #verbosity=2打印调试信息的详细度
runner.run(suite) 
''' 
#3、通过添加类名来运行 
''' 
all_suite=unittest.makeSuite(TestAdd) #添加类名 
runner = unittest.TextTestRunner(verbosity=2) 
runner.run(all_suite)
'''


