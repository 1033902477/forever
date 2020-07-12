import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_mail(report):

    mail_host = ''
    mail_user = ''
    mail_pwd = ''
    sender = ''
    receivers = ['', ''] # 多个接受人，定义一个列表类型

    message = MIMEMultipart()
    message['From'] = Header('test') # 发送者的名字
    message['To'] = Header(','.join(receivers))  # 接受人的名字

    subject = '' # 定义报告的名称
    message['Subject'] = Header(subject, 'utf-8')  # 定义报告的名称
    message_detail = ''  # 定义报告发送的详情
    message.attach(MIMEText(message_detail, 'html', 'utf8'))  # 定义报告中的文本格式以及编码

    # 添加附件
    for i in report:
        report_id = i
        report_apart = MIMEApplication(open(report_id, 'rb').read())
        report_apart.add_header('Content-Disposition', 'attachment', filename=report_id)
        message.attach(report_apart)

    smtp_obj = smtplib.SMTP_SSL(mail_host, '456')  # 456为端口号，根据实际情况填写
    smtp_obj.login(mail_user, mail_pwd)
    smtp_obj.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功... ...')
