'''
hash，哈希，将任意长度的信息压缩到某一固定长度的函数
常见的hash算法有md5和sha1。2这从md4算法上得来的
用于加密有关的操作，主要有SHA1，SHA224，SHA256，SHA384，SHA512，MD5算法。
在python3中已废弃了md5和sha模块。

python中的hashlib提供了这2种的算法 python2.5适用09年停止更新
安装报错，内置，不用安装

md5是一种不可逆的加密算法，目前是最牢靠的算法之一，它对任何字符串都可以加密成一段唯一的固定长度的代码
sha1是由美国标准及数据发布的，也是目前最先及的加密技术，是基于md5改进而来
des是对称加密算法。pydes需要下载pyDes.py拷贝python目录Lib中，pip install pyDes
'''

from pyDes import des, ECB, PAD_PKCS5

import hashlib
import base64


def md5_encode(data):
    m = hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()


def sha1_encode(data):
    sha1 = hashlib.sha1()
    sha1.update(data.encode('utf-8'))
    return sha1.hexdigest()


result1 = md5_encode('重新学习测试')
print('md5加密：', result1)
result2 = sha1_encode('hello,world!')
print('sha1加密：', result2)

# DES加密
'''
语法格式：
pyDes.des(key,[mode],[IV],[pad],[padmode])

key:加密密钥，长度只能为8，必选
mode:加密方式。ECB(默认)、CBC(安全性好于前者)
IV:初始字节数(长度只能为8位)，如果你选择的加密方式为CBC就必须有这个参数，否则可以没有
pad:加密时，将该字符添加到数据的结尾；解密时，将删除从最后一个往前的8位
    如果被加密的数据不是8 bytes的倍数，则pad的数量只能为单数
    如果被加密的数据是8 bytes的倍数，则无所谓
padmode:PAD_NORMAL(可有pad参数)
        PAD_PKCS5(不能有pad参数)
'''


# data为加密数据，key为密钥
def des_encode(data, key):
    k = des(key, mode=ECB, IV=None, pad=None, padmode=PAD_PKCS5)
    # key=des(key,mode=CBC,IV='goodluck',pad='q',padmode=PAD_NORMAL)

    # encrypt加密我的数据，然后进行base64编码
    encodeStr = base64.b64encode(k.encrypt(data))
    return encodeStr


result3 = des_encode('wow', 'abcdefgh')
print('des加密：', result3)
print(str(result3, 'utf-8'))
# 参考https://www.jianshu.com/p/9b7de5ec8b4c


# email
from email.mime.application import MIMEApplication
import email.mime.text
import email.mime.multipart

import smtplib
import base64


# 引入相关模块，主要是处理发送邮件和附件的
# 类


class SendMail:
    def send_mail(self, from1, to, title, content, type='plain', attach=None, pic=None):
        # 生成包含多个邮件体的对象
        msg = email.mime.multipart.MIMEMultipart()
        msg['from'] = from1
        msg['to'] = to
        msg['subject'] = title
        # 邮件正文
        txt = email.mime.text.MIMEText(content, type)
        msg.attach(txt)

        # 文件附件
        if attach != None:
            part = MIMEApplication(open(attach, 'rb').read())
            part.add_header('Content-Disposition','attachment', filename=attach)

            msg.attach(part)

        # jpg图片附件
        if pic != None:
            picpart = MIMEApplication(open(pic, 'rb').read())
            picpart.add_header('Content-Disposition', 'attachment', filename=pic)
            msg.attach(picpart)

            #不造说啥了，上面这个发送出去文件查看异常，后来改成了下面这个好了，原来的代码也没毛病了，备用吧
            # from email.mime.text import MIMEText
            # from email.mime.image import MIMEImage   
            # file_pic=open(pic, 'rb')
            # picpart = MIMEImage(file_pic.read())
            # file_pic.close()
            # picpart.add_header('Content-ID', 'imageid')
            # msg.attach(picpart)

        # 发送邮件

        # 连接服务器，SMTP地址+端口
        smtp = smtplib.SMTP('smtp.163.com', '25')
        # 一般这样
        #     帐户:***@163.com
        # POP3服务器：pop.163.com 端口:110
        # SMTP服务器：smtp.163.com 端口:25
        # smtp=smtplib.SMTP_SSL('smtp.qq.com','465')
        # 设置为调试模式，console 中显示
        smtp.set_debuglevel(1)
        # 登录，用户名+密码，密码可能需要填写授权码
        smtp.login('要发送邮箱的用户名', '密码')#邮箱的用户名，密码
        # 发送，from+to+内容
        smtp.sendmail(from1, to, str(msg))
        # 退出
        smtp.quit()


# 设置变量并调用发送邮件
from1 = '发送出去的邮箱@163.com这里改上面smtp地址也要改，要记得' #发送出去的邮箱
to = '接收的邮箱' #接收的邮箱
# 接收的邮件地址
title = '19-54 title python 全栈自动化测试 文件 行不行 图片'
content = 'content正文 金马奖 金鸡奖 杨天宝'
attach = 'D:\\python_code\\re_Automation\\excel_demo.xlsx'#附件-文件
pic = 'D:\\python_code\\re_Automation\\md_pic\\logging.FileHandler.png'#附件-图片
print('-执行-')

try:
    smtpObj = SendMail()
    smtpObj.send_mail(from1, to, title, content, type='plain', attach=attach, pic=pic)
    print("邮件发送成功")
except smtplib.SMTPException as ex:
    print("Error: 无法发送邮件",ex)



