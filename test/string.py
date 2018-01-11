str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串

print('wa\ng\ng')  # 反斜杠作为转义
print(r'wa\n\ng')  # 在前面加上r让反斜杠正常输出

word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6])
word[0]='m'  # 与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误
