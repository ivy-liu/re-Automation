import requests
import json
'''
url="http://localhost:12306"
path="/book_sim"

full_url=url+path
print("GET请求完整url=",full_url)

params={
    "book_name":"xiaoming",
    "check_status":"on"         
}
print("GET请求参数=",params)

#以json形式提交要写，不写默认以form形式提交
headers={}

r=requests.get(full_url,params=params,headers=headers)
print("GET响应状态码=",r.status_code)
print("GET响应头=",r.headers)#'Content-Type': 'application/json; charset=gbk'
print("GET响应结果（json类型）=",r.text)
print("GET接口的响应时间=",r.elapsed.total_seconds(),'秒')

json_r=r.json()
print("GET响应结果（转为python类型，供后续使用）=",json_r)
'''

'''
url = "http://localhost:12306"
path = "/book_info"

full_url = url+path
print("GET请求完整url=", full_url)

params = {
    "bookname": "接口来自moco",
    "checkstatus": "on"
}
print("GET请求参数=", params)

# 以json形式提交要写，不写默认以form形式提交
headers = {}

r = requests.get(full_url, params=params, headers=headers)
print("GET响应状态码=", r.status_code)
print("GET响应头=", r.headers)  # 'Content-Type': 'application/json; charset=gbk'
print("GET响应结果（json类型）=", r.text)
print("GET接口的响应时间=", r.elapsed.total_seconds(), '秒')

json_r = r.json()
print("GET响应结果（转为python类型，供后续使用）=", json_r)
'''


url = "http://localhost:12306"
path = "/login1"

full_url = url+path
print("GET请求完整url=", full_url)
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "username": "xiaoming",
    "pwd": "123456"
}
print("POST请求参数=", data)


r = requests.post(full_url, data=data, headers=headers)
print("POST响应状态码=", r.status_code)
print("POST响应头=", r.headers)  # 'Content-Type': 'application/json; charset=gbk'
print("POST响应结果（json类型）=", r.text)
print("POST接口的响应时间=", r.elapsed.total_seconds(), '秒')

json_r = r.json()
print("POST响应结果（转为python类型，供后续使用）=", json_r)
