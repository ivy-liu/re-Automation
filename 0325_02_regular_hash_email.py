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

import hashlib
import base64



def md5_encode(data):
    m=hashlib.md5()
    m.update(data.encode('utf-8'))
    return m.hexdigest()


def sha1_encode(data):
    sha1=hashlib.sha1()
    sha1.update(data.encode('utf-8'))
    return sha1.hexdigest()

result1=md5_encode('重新学习测试')
print('md5加密：',result1)
result2=sha1_encode('hello,world!')
print('sha1加密：',result2)

#DES加密
'''
语法格式：
pyDes.des(key,[mode],[IV],[pad],[padmode])

key:加密密钥，长度只能为8，必选
mode:加密方式。ECB(默认)、CBC(安全性好于前者)
IV:初始字节数(长度只能为8位)，如果你选择的加密方式为CBC就必须有这个参数，否则可以没有
pad:加密时，将该字符添加到数据的结尾；解密时，将删除从最后一个往前的8位
    如果被加密的数据不是8 bytes的倍数，则pad的数量只能为单数
    如果被告密的数据是8 bytes的倍数，则无所谓
padmode:PAD_NORMAL(可有pad参数)
        PAD_PKCS5(不能有pad参数)
'''

from pyDes import des,ECB,PAD_PKCS5


#data为加密数据，key为密钥
def des_encode(data,key):
    k=des(key,mode=ECB,IV=None,pad=None,padmode=PAD_PKCS5)
    #key=des(key,mode=CBC,IV='goodluck',pad='q',padmode=PAD_NORMAL)   

    #encrypt加密我的数据，然后进行base64编码
    encodeStr=base64.b64encode(k.encrypt(data))
    return encodeStr

result3=des_encode('wow','12345678')
print('des加密：',result3)