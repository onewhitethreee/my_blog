# 此文件的作用
# 1. 登录到gmail邮箱，读取邮件
# 2. 读取邮件的内容，re匹配出需要的内容
# 3. 判断是否需要回复邮件
# 4. 如果需要回复邮件，回复邮件

import smtplib
import re
import time
import imaplib
from email.mime.text import MIMEText
from email.header import Header
import random
import email
import base64


accout = 'max93685116@gmail.com'
destination = '1135651301@qq.com'
password = 'vdiwghmnzpvznvvd'


def sead_email():
    # Establish a secure session with gmail's outgoing SMTP server using your gmail account
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(accout, password)
    # read a email
    # Send an email
    print('Now i will send a email to ' + destination)

    message = MIMEText('Python script', 'plain', 'utf-8')  # 邮件内容
    message['From'] = Header("Python send email bot", 'utf-8')   # 发送者

    subject = 'Python SMTP 邮件测试'  # 邮件主题
    message['Subject'] = Header(subject, 'utf-8')  # 邮件主题

    server.sendmail(accout, destination, message.as_string())
    # Close the connection
    server.quit()
    print('Email sent!')


def read_email():  # 读取邮件

    conn = imaplib.IMAP4_SSL('imap.gmail.com')
    conn.login(accout, password)

    conn.select('INBOX')
    result, data = conn.search(None, 'ALL')
    mail_id_list = data[0].split()
    mail_id_list.reverse()

    # 在最新邮件上随机选择一个

    random_number_a = random.randint(1, 4)
    random_number_b = random.randint(5, 8)
    random_number_c = random.randint(9, 12)

    # 循环三次，每次随机选择一个邮件
    # 待实现
    for i in mail_id_list[:2]:
        result, data = conn.fetch(i, '(RFC822)')
        if result != 'OK':  # 检查是否有邮件
            print('No messages found!')
            break

        e = email.message_from_bytes(data[0][1])  # 解析邮件

        subject = email.header.make_header(
            email.header.decode_header(e['SUBJECT']))  # 解析邮件主题

        mail_from = email.header.make_header(
            email.header.decode_header(e['From']))  # 解析邮件发件人
        mail_from = str(mail_from).split('<')[1].split('>')[0]  # 解析邮件发件人

        mail_date = email.header.make_header(
            email.header.decode_header(e['Date']))  # 解析邮件时间

        if e.is_multipart():
            # 获取邮件里的内容，它为base64编码，需要解码，[0]表示第一个邮件内容，[1]表示是第二个邮件内容，其内容为相同的内容不过是html格式
            mail_content = e.get_payload()[0].get_payload()
            mail_content = base64.b64decode(mail_content).decode('utf-8')  # 解码
        print("邮件的subject是: %s" % subject)
        print("邮件的发件人是: %s" % mail_from)
        print("邮件的时间是: %s" % mail_date)
        print("邮件的内容是: %s" % mail_content)

        #判断邮件是否为已读

        if 'UNSEEN' in str(e):
            print('这个邮件是未读的')
        else:
            print('这个邮件是已读的')
        print('--------------------------------------')

        if '求文' in str(subject) or '求文' in str(mail_content) and '谢谢' in str(mail_content):
            # 解析链接

            url = re.findall(r'https://(.*)', mail_content)  # 正则表达式匹配出链接
            if len(url) == 0:
                print('没有链接')
                continue
            url = 'https://' + url[0].split('?')[0]  # 链接后面有空格，需要去掉
            print(url)
            if 'xen' in url or 'search' in url or 'zhuanluan' in url:
                print('这个链接不需要回复')
                continue
            else:
                print('这个链接需要回复')
                print('--------------------------------------')
                #回复邮件
                #sead_email()

            continue
        else:
            print('不需要回复邮件,原因是没有求文或者没有谢谢')
            continue

    conn.logout()# 退出邮箱


def main():

    read_email()


if __name__ == '__main__':
    main()


#现有问题
#1. 无法获取最新邮件后面的邮件
#2. 无法判断邮件是否为已读 91-95行可以注释掉
#3. 须对邮件是否已经回复进行判断
