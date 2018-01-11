"""
第一个参数为要打开的文件名。
第二个参数描述文件如何使用的字符。 mode 可以是 'r' 如果文件只读, 'w' 只用于写 (如果存在同名文件则将被删除),
和 'a' 用于追加文件内容; 所写的任何数据都会被自动增加到末尾. 'r+' 同时用于读写。 mode 参数是可选的; 'r' 将是默认值
"""
f=open(r"D:\pythonfile\test.txt","w")
num=f.write("再写点东西")
print("写入的字符数：",num)
num2=f.tell()
print("f.tell()文件对象当前所处位置，字节数",num2)
f.close()

newfile=open(r"D:\pythonfile\test.txt","r")
# str=newfile.read()
str2=newfile.readline()
# print(str)
print("str2:",str2)
newfile.close()