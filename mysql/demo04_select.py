import pymysql

db = pymysql.connect("localhost", "root", "mysqladmin", "example")
cursor = db.cursor()
# SQL 插入语句
sql="select * from employee"
try:
    # 执行sql语句
    cursor.execute(sql)
    results=cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
