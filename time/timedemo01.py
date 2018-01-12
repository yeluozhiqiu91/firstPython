import time

ticks = time.time()
localtime=time.localtime(time.time())
easyreadtime=time.asctime(time.localtime(time.time()))
print("当前时间戳为：", ticks)
print("当地时间：",localtime)
print("易读时间：",easyreadtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))



