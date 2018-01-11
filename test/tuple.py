# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号(())里，元素之间用逗号隔开
tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素,其实就是下标为1和2
print(tuple[2:])  # 输出从第三个元素开始的所有元素，其实就是下标为2及以后的元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组
# tuple[0] = 2  # 改变元组的元素，看看会不会报错
tup1 = ()    # 空元组
tup2 = (20,)  # 一个元素，需要在元素后添加逗号
print(tup1)
print(tup2)
