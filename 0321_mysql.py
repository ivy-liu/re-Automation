import mysql.connector

#连接数据库
try:
    con=mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='vertrigo',
        port=3306,
        database='xiaomingtest',
        charset='utf8',
        buffered=True
    )
    print('数据库连接成功')
    cursor=con.cursor()#获取游标
except mysql.connector.Error as e:
    print('数据库连接失败',str(e))
