---
title: 基于python实现gmail邮件查看，回复
layour: post
tags: [python, gmail, imap, smtplib]
categories: python
index_img: /img/gmail.jpg
date: 2023-01-28 12:25:08
---
# 快速开始

## 相关模块

```
import smtplib #实现邮件的发送
import re #实现正则匹配邮件内容从而发送特定的内容
import time
import imaplib #邮件相关模块
from email.mime.text import MIMEText #邮件相关模块
from email.header import Header #邮件相关模块
import email #邮件相关模块
import base64 #解码相关内容
```

## 代码讲解

```
def sead_email(): #发送邮件函数
    server = smtplib.SMTP("smtp.gmail.com", 587) #创建和gmail服务器的连接
    server.starttls() # 开始连接
    server.login(accout, password) # 进行登录，这里的password不是账号的密码，而是google二次验证给的一个代码
    # read a email
    # Send an email
    print('Now i will send a email to ' + destination) 

    message = MIMEText('Python script', 'plain', 'utf-8')  # 邮件内容
    message['From'] = Header("Python send email bot", 'utf-8')   # 发送者

    subject = 'Python SMTP 邮件测试'  # 邮件主题
    message['Subject'] = Header(subject, 'utf-8')  # 邮件主题

    server.sendmail(accout, destination, message.as_string())
    # Close the connection
    server.quit() #断开连接
    print('Email sent!')
```

### 全局变量

```
accout = ' ' # 自己的邮箱账号
destination = ' ' # 邮箱目的地
password = ' ' # google给的一个二次验证码，需自己主动创建
```

### 读取邮件内容

```
 def read_email():  # 读取邮件

    conn = imaplib.IMAP4_SSL('imap.gmail.com') #进行连接
    conn.login(accout, password) #进行连接

    conn.select('INBOX') # 选择主要信箱
    result, data = conn.search(None, 'ALL') #选择全部
    mail_id_list = data[0].split() 
    mail_id_list.reverse() # 反转一下为了能够获取到最新的邮件，如删了此行会获取到邮箱的第一封邮件

    for i in mail_id_list[:2]: # :2的意思为最新两封邮件，可需改变其他数字来获取到最新10封
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
#################################################################
在这里已经获取到了邮件的主题，内容，发送时间和收件人。
接下来你可以写一个自动回复，根据上方获取的内容，并将read_email里的参数作为返回并传到send_email即可进行发送，只需要修改一下send_email里的内容，标题，收件人，即可实现自动发送邮件，
#################################################################
```
