import smtplib
import email.mime.multipart
import email.mime.text
from djangobook.settings import *

# def sendEmail(Email):
#
#     msg = email.mime.multipart.MIMEMultipart()
#     msgFrom = emailSender  # 从该邮箱发送
#     msgTo = Email  # 发送到该邮箱
#     smtpSever = 'smtp.qq.com'  # 163邮箱的smtp Sever地址
#     smtpPort = '465'  # 开放的端口
#     sqm = emailSmtpSqm  # 在登录smtp时需要login中的密码应当使用授权码而非账户密码
#
#     msg['from'] = msgFrom
#     msg['to'] = msgTo
#     msg['subject'] = 'Python自动邮件-1'
#     content = '''
#     你好:
#         这是一封python3发送的邮件
#     '''
#     txt = email.mime.text.MIMEText(content)
#     msg.attach(txt)
#     smtp = smtplib
#     smtp = smtplib.SMTP()
#     '''
#     smtplib的connect（连接到邮件服务器）、login（登陆验证）、sendmail（发送邮件）
#     '''
#     smtp.connect(smtpSever, smtpPort)
#     smtp.login(msgFrom, sqm)
#     smtp.sendmail(msgFrom, msgTo, str(msg))
#     # s = smtplib.SMTP("localhost")
#     # s.send_message(msg)
#     smtp.quit()
#
# sendEmail("845396799@qq.com")

import smtplib
from email.header import Header
from email.mime.text import MIMEText
import random

# 第三方 SMTP 服务
mail_host = emailHost      # SMTP服务器
mail_user = emailSender                  # 用户名
mail_pass = emailSmtpSqm               # 授权密码，非登录密码
sender = emailSender   # 发件人邮箱(最好写全, 不然会失败)


def sendEmail(receiveEmail):
    content = str(random.randrange(100000, 999999, 1))
    title = 'TravelEasy Eamil Verification Code'
    receivers = [receiveEmail]
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        return content, 0
    except smtplib.SMTPException as e:
        if type(e) == smtplib.SMTPHeloError:
            return content, 1
        if type(e) == smtplib.SMTPAuthenticationError:
            return content, 2
        if type(e) == smtplib.SMTPNotSupportedError:
            return content, 3
        if type(e) == smtplib.SMTPException:
            return content, 4
        if type(e) == smtplib.SMTPRecipientsRefused:
            return content, 5
        if type(e) == smtplib.SMTPSenderRefused:
            return content, 6
        if type(e) == smtplib.SMTPDataErrorr:
            return content, 7
        if type(e) == smtplib.SMTPResponseException:
            return content, 8
        if type(e) == smtplib.SMTPServerDisconnected:
            return content, 9
        if type(e) == smtplib.SMTPConnectError:
            return content, 10
# def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
#     email_client = smtplib.SMTP(SMTP_host)
#     email_client.login(from_account, from_passwd)
#     # create msg
#     msg = MIMEText(content, 'plain', 'utf-8')
#     msg['Subject'] = Header(subject, 'utf-8')  # subject
#     msg['From'] = from_account
#     msg['To'] = to_account
#     email_client.sendmail(from_account, to_account, msg.as_string())
#
#     email_client.quit()

if __name__ == '__main__':
    print(sendEmail("845396799@qq.com"))