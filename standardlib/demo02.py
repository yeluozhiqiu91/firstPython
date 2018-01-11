import smtplib

server = smtplib.SMTP("smtp.qq.com")
server.login("984268356", "password")
server.sendmail('984268356@qq.com', 'wangliujieee@163.com', 'This is a test')
server.quit()
