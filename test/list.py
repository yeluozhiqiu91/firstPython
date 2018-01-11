list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素,其实就是下标为1和2，个人感觉这个让人很费解，直接全部下标不就好了吗，干嘛一个下标，一个第几个元素
print(list[2:])  # 输出从第三个元素开始的所有元素，其实就是从下标为2的元素开始输出后面的所有元素，永远记住前面的是下标
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表

# 与Python字符串不一样的是，列表中的元素是可以改变的：
a = [1, 2, 3, 4, 5, 6]
a[0]=9
print(a)
a[2:5]=[12,13,14]
print(a)