from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.set_window_size(1333,888)

# driver.get('https://www.baidu.com/')
# #href属性包含连接元素
# driver.find_element_by_xpath("//a[contains(@href,'refer=888')]").click()#http://e.baidu.com/?refer=888



'''
#弹窗 alert confirm promp弹窗

driver.get('file:///D:/python_code/re_Automation/tanchuang01.html')
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


#frame处理

#frame 标签有 frameset、frame、iframe 三种，frameset 跟其他普通标签的定位没有区别。
# 而 frame 与 iframe 对 selenium定位而言是一样的，他们都通过 se 提供的特定方 法来进行定位。
# 最常用的三种方法如下： 
#  driver.switch_to.frame(frame 的 id 或者 name 属性值)#切换 frame 
#  driver.switch_to.parent_frame()#遇到嵌套的 frame，从子 frame 切回到父 frame。
类似HTML 代码：
<html> 
    <iframe id="frame1"> 
        <iframe id="frame2" / >
        </iframe>242424
</html> 
#  driver.switch_to.default_content()#从 frame 中切回主文档

























time.sleep(5)
driver.quit()