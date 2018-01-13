# 根据输入的行数，列数，最小和最大值随机生成网格状的数据
import random


def get_int(msg, minimum, default):  # 提示信息，最小值，默认值
    while True:
        try:
            line = input(msg)
            if not line and default is not None:  # 如果没有输入任何值但默认值不是None就返回默认值
                return default
            i = int(line)
            if (i < minimum):  # 如果输入的值小于最小值就提示，否则返回输入的值
                print("must be>=", minimum)
            else:
                return i
        except ValueError as err:
            print(err)


rows = get_int("rows:", 1, None)
columns = get_int("columns:", 1, None)
minimum = get_int("mininum (or Enter for 0)", -100000, 0)
defaultmax = 1000  # 设置默认的最大值
if defaultmax < minimum:
    defaultmax = minimum * 2
maximum = get_int("maximum (or Enter for" + str(defaultmax) + "):",minimum, defaultmax)
row = 0
while row < rows:
    line = ""
    column = 0
    while column < columns:
        i = random.randint(minimum, maximum)
        s = str(i)
        while len(s) < 10:  # 不足10位就在前面补空格
            s = " " + s
        line += s
        column += 1
    print(line)
    row += 1
