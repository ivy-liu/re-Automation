from selenium import webdriver
import time

#创建se驱动
driver=webdriver.Chrome()
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time


# # 打开浏览器，同时打开首页
url = 'https://jc-lab.yscredit.com/'
# # driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
# driver = webdriver.Chrome()#上面一行没问题
driver.get(url)

#浏览器最大化
driver.maximize_window()
#设置宽高
driver.set_window_size(1333,888)

#获取窗口标题
print('窗口标题是-',driver.title)


#截图
path='screenshot_pic//'+'1.png'
driver.get_screenshot_as_file(path)

#刷新
driver.refresh()
time.sleep(5)
driver.get('https://www.lizhi.fm/user/2525632519289351212')
print('窗口标题是-',driver.title)


# time.sleep(5)
# driver.back()#后退

# time.sleep(5)
# driver.forward()#前进

time.sleep(5)


#关闭单个窗口-close
# driver.close()
#关闭所有窗口-quit
# driver.quit()

'''
#以搜索框为例子，匹配
driver.get('http://xqtesting.com/')
driver.find_element_by_id('words').send_keys('大数据测试')
driver.find_element_by_class_name('btn-default').click()

time.sleep(5)

driver.find_element('id','words').send_keys('自动化测试')
driver.find_element('class name','btn-default').click()

time.sleep(5)

#清空
driver.find_element('id','words').send_keys('清空了吗')
time.sleep(3)
driver.find_element('id','words').clear()
time.sleep(3)
'''

'''
#超链接
#精确匹配
driver.get('http://xqtesting.com/')
driver.find_element_by_link_text('宝妈店铺').click()
time.sleep(5)

#模糊匹配
driver.find_element_by_partial_link_text('正品').click()
time.sleep(5)
'''


#xpath
driver.get('http://xqtesting.com/')
