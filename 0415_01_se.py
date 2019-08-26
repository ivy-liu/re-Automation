from selenium import webdriver
import time

#创建se驱动
driver=webdriver.Chrome()
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time


# # 打开浏览器，同时打开首页
# url = 'https://jc-lab.yscredit.com/'
# # driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
# driver = webdriver.Chrome()#上面一行没问题
# driver.get(url)

# #浏览器最大化
# driver.maximize_window()
#设置宽高
driver.set_window_size(1333,888)

# #获取窗口标题
# print('窗口标题是-',driver.title)


# #截图
# path='screenshot_pic//'+'1.png'
# driver.get_screenshot_as_file(path)

# #刷新
# driver.refresh()
# time.sleep(5)
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
# driver.get('https://www.lizhi.fm/')
# 关于 xpath 的使用可以用如下几种方式进行定位： 
# 1）首推使用使用火狐下的 firepath 插件，简单、快捷、高效。chrome 下是先识别到
# 元素的 html 代码在右键 copy>copy xpath 即可。
# 2）自己手写 xpath 路径。一般语法格式为
# //标签名[@属性名=属性值] 或者 //*[@属性名=属性值]
# 区别在于是否有指定的标签

#绝对定位
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/a/img").click()

time.sleep(5)

# #利用元素属性定位
# driver.find_element_by_xpath(".//*[@id='js-obsBtn']").click()
# time.sleep(5)

#层级和属性结合
driver.find_element_by_xpath("//*[@id='promoRadio']/div[3]/ul/li[1]/a/img").click()
time.sleep(5)

#使逻辑运算符 这个木有
# driver.find_element_by_xpath(".//*[@class='audioName'and@class='form-control']")

driver.get('https://www.guokr.com/')

# driver.get('http://xqtesting.com/')

#匹配部分属性  stars-with  ends-with
# #查找id属性中开始位置包含‘nice'关键字的页面元素
# driver.find_element_by_xpath("//input[starts-with(@id,'nice')]")
# driver.find_element_by_xpath("//input[ends-with(@id,'nice')]")

#查找input标签 placeholder属性中包含'搜索'关键字的页面元素
driver.find_element_by_xpath("//input[contains(@placeholder,'搜索')]").click()#选中搜索连输入框
# driver.find_element_by_xpath("//span[contains(@class,'styled__ImageFilterMask-sc-1mpyx4-1 gKJlUN')]")
time.sleep(5)

#text()
driver.find_element_by_xpath("//*[@id='app']") 3