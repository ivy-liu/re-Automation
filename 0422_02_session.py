


import  requests

def login():
   '''登录接口:/auth/login'''
   s=requests.Session()
   r=s.post(
      url='http://11X.39.63.XX:20080/auth/login',
      data={'username':'system','password':'123456'})
   return s

def selectable():
   r=login().get(url='http://11X.39.63.XX:20080/depot/parks/selectable')
   print (r.status_code)
   print (r.text)

selectable()

# requests.Session().get(url)
# requests.Session().post(url)



'''
再次执行如上的代码，见执行后的打印内容：

200
{
  "data": [
    {
      "Text": "\u65b0\u957f\u5b89\u5e7f\u573a\u9053\u8fb9\u505c\u8f66", 
      "Value": 1
    }
  ]
}
'''




import requests
'''在登陆模块创建一个全局session，在其他接口操作时带入登陆时的session，保持session的一致性'''
s = requests.Session()#定义一个全局session
class testlogin():
  login_url = "http://api-xxxxxx/api/Account/Login"
  username = "xxxxx"
  password = xxxxx
  def test_login(self):
  data ={
    "UserName" : self.username,
    "Password" : self.password
  }
  r = s.post(self.login_url,data)
  print(r.cookies)
  return s


from test_case.loggin import testlogin
import unittest
 
'''这里导入之前的登陆模块，调用登陆模块的session，然后去执行其他接口'''
s = testlogin().test_login()
 
class testtransfer(unittest.TestCase):
 def setUp(self):
  self.transfer_url = "http://xxxxxxx/Transfer/DoTransferToGame"
 def test_transfer(self):
  url = self.transfer_url
  data ={"Amount":xx,
    "GamePlatform":"xxxx"
    }
  r = s.post(url,data)
 
  print(r.text)
