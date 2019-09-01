


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