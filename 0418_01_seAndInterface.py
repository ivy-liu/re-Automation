#cookies(传值、profile) ，
# 上传下载，
# 参数化，
# 视频播放 ，
# 日期元素，
# 截图，
# 表格
#https
#等待方式（强制、隐形-页面加载、显性-元素加载）
#饼状图


from selenium import webdriver
import time

# driver=webdriver.Chrome()


#cookies
'''
1. 万能验证码 or 去掉验证码 
2. 手工介入（需要输入的地方 sleep 一会） 
3. 利用 cookies 来实现（问开发哪个 cookies 值是登录后需要的，把这个值带上即可）， 常见的方法如下： 
 driver.get_cookies()#获取 cookies 
 driver.get_cookie(name)#返回字典的 key 为"name"的 cookie 信息 
 driver.add_cookie({'name': 'key-aaa', 'value': 'key-bbb'}) 
 driver.delete_all_cookies()#删除 cookies
'''

'''
bduss_chrome='VIQUVWd35pS3M3Q1FSRXhNa2NtLWw1dS1SQkkzaUJpU3VoR05lQzRjaXhjSTlkSUFBQUFBJCQAAAAAAAAAAAEAAADwEwkqwfXWrrW6AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALHjZ12x42ddOF'

driver.get('https://www.baidu.com')
#设置cookies的值，问开发，自己找要累死
c1={'domain':'.baidu.com',    #服务器域名
    'name':'BDUSS',    #cookie的名称
    'value':bduss_chrome,    #cookie
    'path':'/',    #那些路径的页面下可以获取服务器设置的cookie
    'httpOnly':True,    #防止脚本攻击
    'secure':False    #只有为https时浏览器猜才向服务器提交响应的cookie
}
driver.add_cookie(c1)#添加cookies
print('添加cookies')
time.sleep(3)
driver.refresh()
driver.implicitly_wait(5)
time.sleep(3)
'''

#profile文件
#首先需要手工登入1次，且勾选记住信息，相当于浏览器的保存表单的功能
#路径获取 浏览器->帮助->故障排除信息->显示文件夹
#有时效性，长了就失效了
#----火狐------
# profile_ff=r"火狐的路径" #不要忘记r
# fp=webdriver.FirefoxProfile(profile_ff)
# driver=webdriver.Firefox(fp)

# driver.get('http://www.baidu.com')
# time.sleep(5)
# driver.quit()
    # #------ chrome-----
    # #chrome的，chrome://version/ 查看自己的“个人资料路径”
    # #个人资料路径	C:\Users\ivy\AppData\Local\Google\Chrome\User Data\Default
    # #路径取到User Data，不到Default
    # profile_ff=r"user-data-dir=C:\\Users\\ivy\\AppData\\Local\\Google\\Chrome\\User Data"
    # #加载配置
    # option=webdriver.ChromeOptions()
    # option.add_argument(profile_ff)
    # #初始化启动浏览器配置
    # # driver=webdriver.Chrome(chrome_options=option)这个也行
    # driver=webdriver.Chrome(options=option)
    # time.sleep(3)
    # driver.get('http://www.baidu.com')
    # time.sleep(5)
    # driver.quit()


# 上传下载


#上传
# 标准的<input type='file' name='file'>
# driver.find_element('name','file').send_keys('要上传的文件路径')
# 非标准的上传
# http://www.xqtesting.com/blog/selenium-webdriver-90.html

#下载

#指定下载路径
# profile_ff=r"user-data-dir=C:\\Users\\ivy\\AppData\\Local\\Google\\Chrome\\User Data"
# profile=webdriver.FirefoxProfile(profile_ff)火狐操作


'''
#火狐
url='https://www.lizhi.fm/helper/download'
from selenium import webdriver
import os,time
 
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList",0)
fp.set_preference("browser.download.manager.showhenStarting",True)
fp.set_preference("browser.download.dir",os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","binary/octet-stream")#下载文件类型
 
driver = webdriver.Firefox(firefox_profile = fp)
driver.get(url)
#选择下载文件
driver.find_element('link text','下载').click()
time.sleep(5)
'''

'''
#谷歌
options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
options.add_experimental_option('prefs', prefs)
 
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.lizhi.fm/helper/download")
driver.find_element('link text','下载').click()
time.sleep(5)#需要时间长一点，怕下载不完
#下载在d:\\
'''


# #参数化 https://www.cnblogs.com/hanxiaobei/p/7340429.html
# #文件txt
# import codecs
# #打开文件utf-8
# source=codecs.open('test_folder\parameter.txt','r','utf-8')
# context=source.readlines()#多行读取

# value01=list(context)
# print('value01-',value01)#value01- ['18352543210\r\n', '啥啥密码123']

# value03=[]
# value03.extend(context)
# print('value03-',value03)#value03- ['18352543210\r\n', '啥啥密码123']

# source=codecs.open('test_folder\parameter.txt','r','utf-8')
# value02 =[]
# while True:
#     context = source.readline()#按行读取
#     value02.append(context)
#     if len(context) ==0:
#         break
# print('readline格式:',type(value02))
# print('value02-',value02)#['18352543210\r\n', '啥啥密码123', '']

# source=codecs.open('test_folder\parameter.txt','r','utf-8')
# context = source.read()#一次性读取，赋值给字符串
# value04=list(context)
# print('value04-',value04)#['1', '8', '3', '5', '2', '5', '4', '3', '2', '1', '0', '\r', '\n', '啥', '啥', '密', '码', '1', '2', '3']



#写在字典里
# for username,passwd in info.items():
#     print(username)
#     print(passwd)

#写在excel里
# D:\python_code\re_Automation\0321_mysql_and_excel.py
# 写完就忘。。。想死！

'''
#视频播放 http://videojs.com/
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('http://videojs.com/')

video=driver.find_element_by_xpath('.//*[@id="preview-player_html5_api"]')
url=driver.execute_script('return arguments[0].currentSrc;',video)
print('播放地址--',url)
duration=driver.execute_script('return arguments[0].duration;',video)
print('播放时长-',duration)

print('--播放--')
driver.execute_script('return arguments[0].play()',video)
time.sleep(10)

print('--暂停--')
driver.execute_script('arguments[0].pause()',video)
time.sleep(10)

#日期元素
js='document.getElementById("txtBeginDate").removeAttribute("readonly")'
driver.execute_script(js)

#最好先清空后传值
driver.find_element('id','txtBeginDate').clear()
driver.find_element('id','txtBeginDate').send_keys('2019-11-11')
time.sleep(5)

# #另一种方法
# js='document.getElementById("txtBeginDate").value="2019-09-09"'
# driver.execute_script(js)
'''

#截图
# driver.get_screenshot_as_file("保存的路径地址")

'''
#表格
driver=webdriver.Chrome()
driver.get('file:///D:/python_code/re_Automation/test_folder/table.html')
table=driver.find_element_by_xpath("html/body/table/tbody")

# table的总行数，包括标题
table_rows=table.find_elements('tag name','tr')
print('总行数-',len(table_rows))#总行数- 4

#table的总列数
table_cols=table_rows[0].find_elements('tag name','td')
print('总列数-',len(table_cols))#总列数- 3

#获取某单元格的文本，下标取值
row2_col2=table_rows[1].find_elements('tag name','td')[1].text
print('第二行第二列-',row2_col2)#第二行第二列- row 2, cell 2
'''


#https
#一般情况不需要处理，特殊https需要处理
#对于 firefox： 
# profile = webdriver.FirefoxProfile() 
# profile.accept_untrusted_certs = True 
# driver = webdriver.Firefox(firefox_profile=profile) 
# driver.get('https://www.cacert.org/') 
# driver.close()
#chrome:
option=webdriver.ChromeOptions()
option.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(chrome_options=option)
driver.get('https://www.cacert.org/')
time.sleep(10)


'''
#等待方式
#显性等待-until、until_not
from selenium.webdriver.support.wait import WebDriverWait#等元素加载，显性等待
WebDriverWait(driver,5).until(lambda diver:driver.find_element('link text','退出'))
'''

#生成饼状图
from openpyxl.chart import PieChart,Reference
from openpyxl import load_workbook
import os
os.chdir('D:\\python_code\\re_Automation\\test_folder\\testcase_study.xlsx')

def pie_chert(wb):
    table=wb.get_sheet_by_name(wb.get_sheet_by_name()[0])

    #生成饼图对象
    pie=PieChart()
    #图的标题
    pie.title='接口测试统计'
    #获取标签 第1列，2行到3行
    labels=Reference(table,min_col=1,min_row=2,max_col=1,max_row=3)
    # 获取数据，这里需要注意，上面必须多取1行空的，excel系列导致   
    # 第2列1到3行，实际：第2列2到3行
    data=Reference(table,min_col=2,min_row=1,max_col=2,max_row=3)

    #添加数据和标签到图表里
    pie.add_data(data,titles_from_data=True)
    pie.set_categories(labels)

    #添加图表到sheet里
    table.add_chart(pie,'A10')

    #保存excel
    wb.save('D:\\python_code\\re_Automation\\test_folder\\testcase_study.xlsx')

wb=load_workbook('D:\\python_code\\re_Automation\\test_folder\\testcase_study.xlsx')
pie_chert(wb)