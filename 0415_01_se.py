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
# driver.get('https://www.lizhi.fm/user/2525632519289351212')
# print('窗口标题是-',driver.title)


# time.sleep(5)
# driver.back()#后退

# time.sleep(5)
# driver.forward()#前进

# time.sleep(5)


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

# #绝对定位
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/a/img").click()

# time.sleep(5)

# #利用元素属性定位
# driver.find_element_by_xpath(".//*[@id='js-obsBtn']").click()
# time.sleep(5)

# #层级和属性结合
# driver.find_element_by_xpath("//*[@id='promoRadio']/div[3]/ul/li[1]/a/img").click()
# time.sleep(5)


# driver.get('https://www.guokr.com/')
#使逻辑运算符 这个木有
# driver.find_element_by_xpath(".//*[@class='more'and@href='https://www.guokr.com/zone/#special']").click()

# driver.get('https://www.guokr.com/')

# driver.get('http://xqtesting.com/')

#匹配部分属性  stars-with  ends-with
# #查找id属性中开始位置包含‘nice'关键字的页面元素
# driver.find_element_by_xpath("//input[starts-with(@id,'nice')]")
# driver.find_element_by_xpath("//input[ends-with(@id,'nice')]")

# #查找input标签 placeholder属性中包含'搜索'关键字的页面元素
# driver.find_element_by_xpath("//input[contains(@placeholder,'搜索')]").click()#选中搜索连输入框
# time.sleep(5)

#text()
# driver.get('https://www.guokr.com/')
# driver.find_element_by_xpath("//*[@class='styled__AccountWrap-sc-16f3awt-0 jtkvlE']/li[text()='注册']").click()
# driver.find_element_by_xpath("//*[@id='siteNav']/a[text()='注册']").click()
# time.sleep(5)

'''
* 代表任意标签，没有指定标签的时候使用
. 代表选区当前节点
.. 代表选区当前节点的父节点

'''

'''
#text :获取元素文本
# driver.get('https://www.guokr.com/institute')
driver.implicitly_wait(5)
# textvalue=driver.find_element_by_class_name("layout__Skeleton-zgzfsa-3 styled__InfoSummaryWrap-w0pb7j-10 gcAVkH").find_element_by_xpath("ul/li[3]/a").text
textvalue=driver.find_element_by_xpath("//*[@class='layout__Skeleton-zgzfsa-3 styled__InfoLabelWrap-w0pb7j-6 jSKFQp']/span[1]").text
print('textvalue--',textvalue) #textvalue-- 科学人
time.sleep(5)

#tag_name :获取元素标签  神奇 没有这个方法了
tagname=driver.find_element_by_xpath("//*[@class='layout__Skeleton-zgzfsa-3 styled__InfoLabelWrap-w0pb7j-6 jSKFQp']/span[1]").tag_name
print('tagname--',tagname) #tagname-- span
time.sleep(5)

#is_displayed()判断元素是否存在  这个方法有毛病，存在返回true，不存在就报错过不去了
r=driver.find_element_by_xpath("//*[@class='styled__AccountWrap-sc-16f3awt-0 jtkvlE']/li[text()='注册']").is_displayed()
print(r)
time.sleep(5)

#get_attribute()：获取元素的其他属性
getAttribute=driver.find_element_by_xpath("//*[@class='layout__Skeleton-zgzfsa-3 styled__InfoLabelWrap-w0pb7j-6 jSKFQp']/span[1]").get_attribute('outerHTML')
print('get_attribute--',getAttribute) #get_attribute-- <span>科学人</span>
time.sleep(5)
'''


#css定位 不好用 记不住 以后不考虑这个东西
# driver.find_element_by_css_selector('#words')



driver.get('https://form.teambition.net/f/xtqUHj?x_field_1=demo_tour')
driver.implicitly_wait(5)

#一组元素的定位
#cheeckbox 复选框
# inputs=driver.find_elements_by_tag_name('input')
# for input in inputs:
#     if input.get_attribute('type')=='checkbox':
#         input.click()
# time.sleep(5)
# driver.quit()

# driver.find_element_by_class_name("select2-selection__rendered").click()
# time.sleep(3)
# driver.find_element_by_xpath("/html/body/span/span/span[2]/ui/li[4]").click()#选中id结尾lCVp
# time.sleep(3)
# driver.find_element_by_xpath(".//*[@id='select2-entry_field_15-result-jhi2-cmuo']").click()
# #不通


# #下拉框 可以正常使用
# from selenium.webdriver.support.ui import Select
# # Select(driver.find_element_by_id("entry_field_10")).select_by_index(1)#下表从0开始
# # Select(driver.find_element_by_id('entry_field_10')).select_by_value('2Nh7')
# Select(driver.find_element_by_id('entry_field_10')).select_by_visible_text('300+')












time.sleep(5)
driver.quit()