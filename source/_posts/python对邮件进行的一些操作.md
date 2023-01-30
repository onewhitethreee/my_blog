---
title: 基于python实现gmail邮件查看，回复
layour: post
uuid: 0c449140-a0ad-11ed-b6de-e73c5841cd31
tags: [python, gmail, imap, smtplib]
categories: python
index_img: /img/gmail.jpg
date: 2023-01-29 18:07:08
---
---

# imaplib的一些操作

```
    conn = imaplib.IMAP4_SSL('imap.gmail.com')
    conn.login(accout, password)
    print(conn.list()) #即可打印下方内容，只要在select里填入/后面的内容就能进行对应的操作
    # print(conn.list())# 打印邮箱所有文件夹
    # conn.select('INBOX') # 选择收件箱
    # [b'(\\HasNoChildren) "/" "INBOX"',  # 收件箱
    # b'(\\HasChildren \\Noselect) "/" "[Gmail]"',  # 未读邮件
    # b'(\\HasNoChildren \\Junk) "/" "[Gmail]/&V4NXPpCuTvY-"' # 垃圾邮件
    # b'(\\HasNoChildren \\Trash) "/" "[Gmail]/&XfJSIJZkkK5O9g-"' # 垃圾箱
    # b'(\\Flagged \\HasNoChildren) "/" "[Gmail]/&XfJSoGYfaAc-"' # 星标
    # b'(\\HasNoChildren \\Sent) "/" "[Gmail]/&XfJT0ZCuTvY-"' # 已发送
    # b'(\\All \\HasNoChildren) "/" "[Gmail]/&YkBnCZCuTvY-"' # 所有邮件
    # b'(\\Drafts \\HasNoChildren) "/" "[Gmail]/&g0l6Pw-"' # 草稿
    # b'(\\HasNoChildren \\Important) "/" "[Gmail]/&kc2JgQ-"'] # 重要邮件
```
