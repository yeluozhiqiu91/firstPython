import pymysql

db = pymysql.connect("localhost", "root", "mysqladmin", "example")
cursor = db.cursor()
# SQL 插入语句
sql="delete from employee where age>22"
try:
    # 执行sql语句
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()

# 关闭数据库连接
db.close()
