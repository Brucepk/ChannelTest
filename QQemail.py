# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time


def sendMail(report_file):
    # 创建一个带附件的实例
    msg = MIMEMultipart()
    file = open(report_file, 'rb').read()
    att1 = MIMEText(file, _charset='utf-8')
    att1["Content-Type"] = 'application/octet-stream'  # 二进制流数据
    # attachment（意味着消息体应该被下载到本地；大多数浏览器会呈现一个“保存为”的对话框，将filename的值预填为下载后的文件名
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att1)

    # 发送邮箱地址
    sender = '1441791089@qq.com'
    # 邮箱授权码，非登陆密码
    password = 'oazzokjcjpvofjgc'
    # 收件箱地址
    receiver = ['838033620@qq.com', '1441791089@qq.com']
    # smtp服务器
    smtp_server = 'smtp.qq.com'
    # 发送邮箱地址
    msg['From'] = sender
    # 收件箱地址
    msg['To'] = ','.join(receiver)
    # 主题
    msg['Subject'] = '自动化测试结果-' + time.strftime("%Y-%m-%d %H_%M_%S")
    server = smtplib.SMTP(smtp_server, 25)

    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())
    server.quit()


if __name__ == '__main__':
    sendMail(r'D:\PycharmProjects\report.html')
