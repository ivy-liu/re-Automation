#单文件夹
'''
主程序入口
遍历接口，发送请求，接受响应，判断结果
保存结果（生成报告）
发送email
log日志
================
项目根目录
    main.py 功能调用
    src
        1.py遍历所有课执行case
        2.py请求的发送、响应接受、结果判断
    log
    testcase
    testdata excel文件
    reports 
    commons 模块请求响应类 日志类 发送Email的模块 发送报告
    libs 插件

伪代码

src
    run_testcase.py--完成遍历所有课执行case
    interface_test.py--每次遍历都调用请求-响应-判断
    调用http请求响应类，对结果进行判断，print

import 请求类
class InterfaceTest:
    def interface_test(self,入参列表)：
        http=请求类()
        status_code,response,time=http.post_form(入参列表)

        if status_code==200:
            if re.sreach(error_code,response):
                print()

            else:
        else:
接口字段定义
it=InterfaceTest()
it.interface_test(入参列表)
