import pymysql

db = pymysql.connect("localhost", "root", "mysqladmin", "example")
cursor = db.cursor()
# SQL 插入语句
sql="update employee set age=age+1 where sex='%c'"%('M')
try:
    # 执行sql语句
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

# 关闭数据库连接
db.close()
