import pymysql

db = pymysql.connect("localhost", "root", "mysqladmin", "example")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print("DataBase Version:%s" % (data))
db.close()
