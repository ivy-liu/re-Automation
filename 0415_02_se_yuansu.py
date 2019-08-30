from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.set_window_size(1333,888)


#弹窗、frame、多窗口、屏幕滚动、js操作、断言、



# driver.get('https://www.baidu.com/')
# #href属性包含连接元素
# driver.find_element_by_xpath("//a[contains(@href,'refer=888')]").click()#http://e.baidu.com/?refer=888



'''
#弹窗 alert confirm promp弹窗

driver.get('file:///D:/python_code/re_Automation/test_folder/tanchuang01.html')
driver.implicitly_wait(5)

#alert

driver.find_element_by_id('alert').click()
time.sleep(2)
#获取alert对话框
alert_01=driver.switch_to.alert
time.sleep(2)
#打印对话框内容
print(alert_01.text)
#alert对话框是警告对话框，只有接受弹窗
alert_01.accept()
time.sleep(2)


#confirm

driver.find_element_by_id('confirm').click()
time.sleep(2)
#获取confirm对话框
confirm_01=driver.switch_to.alert
time.sleep(2)
#打印对话框内容
print(confirm_01.text)
#confirm对话框可选accept或dissmiss
# confirm_01.accept()
confirm_01.dismiss()
time.sleep(2)

#prompt
driver.find_element_by_id('prompt').click()
time.sleep(2)

#获取prompt对话框
prompt_01=driver.switch_to.alert
time.sleep(2)
#打印对话内容
print(prompt_01.text)
#在对话内输入信息
confirm_01.send_keys('ivy-liu')
#点击确认按钮，提交输入的内容
prompt_01.accept()

'''

'''
#虚拟鼠标键盘
driver.get('http://www.xqtesting.com')
driver.implicitly_wait(5)

#模拟鼠标悬浮
from selenium.webdriver.common.action_chains import ActionChains
m=driver.find_element("link text","培训课程")
ActionChains(driver).move_to_element(m).perform()
time.sleep(5)
driver.find_element('partial link text','常见问题').click()
driver.implicitly_wait(5)

#模拟键盘
from selenium.webdriver.common.keys import Keys
n=driver.find_element('id','words')
ActionChains(driver).move_to_element(n).perform()#鼠标悬浮
ActionChains(driver).double_click(n).perform()#鼠标双击
ActionChains(driver).click_and_hold(n).perform()#鼠标右击
'''

#frame处理

#frame 标签有 frameset、frame、iframe 三种，frameset 跟其他普通标签的定位没有区别。
# 而 frame 与 iframe 对 selenium定位而言是一样的，他们都通过 se 提供的特定方法来进行定位。
# 最常用的三种方法如下： 
#  driver.switch_to.frame(frame 的 id 或者 name 属性值)#切换 frame 
#  driver.switch_to.parent_frame()#遇到嵌套的 frame，从子 frame 切回到父 frame。
# 类似HTML 代码：
# <html> 
#     <iframe id="frame1"> 
#         <iframe id="frame2" / >
#         </iframe>
# </html> 
#  driver.switch_to.default_content()#从 frame 中切回主文档

'''
driver.get("file:///D:/python_code/re_Automation/test_folder/iframe.html")
# 1.通过id定位
driver.switch_to.frame('frame1')
# # 2.通过name定位
# driver.switch_to.frame('myframe')
# # 3.用WebElement对象来定位
# driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))  
# # 4.通过index定位，第一个是0
# driver.switch_to.frame(0)

driver.find_element('link text','一行文字点击到达百度').click()
#后面需要完整超链接文字
'''




# '''
# 业务：
# 访问荔枝官网，点击导航“下载直播助手”，之后会新窗口打开

# 基本逻辑：
# 访问官网获得句柄
# ->打开新窗口获得所有句柄
# ->for循环排除当前句柄，另一个是原页面句柄
# '''
# driver.get('https://www.lizhi.fm/')#打开官网
# driver.implicitly_wait(5)
# driver.find_element('id','js-obsBtn').click()#打开下载页面
# driver.implicitly_wait(5)

# #新窗口打开
# # new_win='window.open("http://www.xqtesting.com");'
# # driver.execute_script(new_win)


# #获取当前窗口句柄-官网
# old_handle=driver.current_window_handle

# #获取当前窗口句柄集合（应该是2个）列表类型
# handles=driver.window_handles
# print(handles)

# #获取新打开的窗口-下载页面
# new_handle=None
# for handle in handles:
#     if handle!=old_handle:
#         new_handle=handle


# driver.switch_to.window(new_handle)
# print('现在在:',driver.title,'\n--','new_handle:',new_handle)
# time.sleep(3)
# driver.switch_to.window(old_handle)
# print('现在在:',driver.title,'\n--','old_handle:',old_handle)

 


#js应用

'''
#屏幕滚动

driver.get('https://www.lizhi.fm/')#打开官网
driver.implicitly_wait(5)
time.sleep(3)
print('driver.name--',driver.name)

# 类型的判断不对 document.documentElement.scrollTop chrome可以执行
# #回到顶部
# def scroll_top(driver):
#         print('回到顶部-')
#         if driver.name=="chrome":
#                 js='var q=document.body.scrollTop=0'
#         else:
#                 js='var q=document.documentElement.scrollTop=0'
#         driver.execute_script(js)
        

# #滚到底部
# def scroll_foot(driver):
#         print('滚到底部-')
#         if driver.name=='chrome':
#                 js='var q=document.body.scrollTop=10000'
#         else:
#                 js='var q=document.documentElement.scrollTop=10000'
#         driver.execute_script(js)
# scroll_foot(driver)
# time.sleep(3)
# scroll_top(driver)


# 这个没毛病
#滚到底部
js='var q=document.documentElement.scrollTop=10000'
driver.execute_script(js)
time.sleep(3)
#回到顶部
js='var q=document.documentElement.scrollTop=0'
driver.execute_script(js)



# from selenium.webdriver.common.keys import Keys #引入键盘
# #xpath 定位然后使用键盘向下按键进行滚动
# driver.find_element_by_xpath("//*[@class='modal-right']").send_keys(Keys.DOWN)
#  ———————————————— 
# 版权声明：本文为CSDN博主「学艺的海盗」的原创文章，遵循CC 4.0 by-sa版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/qq_41370110/article/details/80865886



# # 向下滚动200个像素
# driver.execute_script('window.scrollBy(0,200)')

# time.sleep(2)
# # 滚动至元素ele可见位置
# eles = driver.find_elements_by_css_selector('#rs table tr th a')
# ele = eles[0]
# driver.execute_script("arguments[0].scrollIntoView();",ele)

# time.sleep(2)
# # 向右滚动200个像素
# driver.execute_script('window.scrollBy(200,0)')
# 原文连接：https://www.cnblogs.com/wilson-5133/p/10996810.html
'''

'''
#js改动元素属性
driver.get('https://www.baidu.com/')#打开官网
driver.implicitly_wait(5)
driver.find_element('link text','登录').click()
driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
time.sleep(4)
#把按钮隐藏  这里有个分号
driver.execute_script('document.getElementById("TANGRAM__PSP_10__submit").type="hidden";')
print('driver.title',driver.title)
try:
        assert '百度一下' in driver.title
        print('对，没毛病！')
except Exception as e:
        print('有问题',e)


'''

#打开网页，登陆，断言
driver=webdriver.Chrome()
driver.set_window_size(1333,888)
driver.get('http://xqtesting.com/index.html')
driver.implicitly_wait(5)



driver.find_element('link text','登录').click()
driver.find_element_by_id('account').send_keys('---账号--')#账号
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='password']").send_keys('--密码--')#密码
time.sleep(3)
driver.find_element_by_xpath("//*[@class='btn btn-primary btn-wider btn-lg btn-block'and@type='submit']").click()#登入

driver.implicitly_wait(5)#等页面加载，隐性等待

from selenium.webdriver.support.wait import WebDriverWait#等元素加载，显性等待
WebDriverWait(driver,5).until(lambda diver:driver.find_element('link text','退出'))



myname=driver.find_element_by_xpath('.//*[@id="siteNav"]/a[1]').text
print('myname--',myname)
try:
        assert'刘婉莹' in myname
        print('对，没毛病！是我~')
except Exception as e:
        print('有问题',e)

time.sleep(5)
driver.quit()