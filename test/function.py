def hello():
    print("hello")


hello()


def area(width, height):
    return width * height


print(area(3, 2))


def changeInt(a):
    a = 10


b = 2
changeInt(b)
print(b)


# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print("函数外取值: ", mylist)
