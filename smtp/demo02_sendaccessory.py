import smtplib, sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "984268356@qq.com"  # 用户名
mail_pass = "euclbwkeldlubbih"  # 口令

sender = '984268356@qq.com'
receivers = ['wangliujieee@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
content = '''
<p>Python 邮件发送测试,带附件的。。。</p>
'''

message = MIMEMultipart()
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件 发附件测试'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText(content, 'plain', 'utf-8'))
# 构造附件1，传送相应目录下的 test.txt 文件
att1 = MIMEText(open(r'D:\pythonfile\test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)

# 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open(r'D:\pythonfile\test2.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="test2.txt"'
message.attach(att2)
try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
    print(sys.exc_info()[0], sys.exc_info()[1])
