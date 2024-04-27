---
title: GITHUB webHook 使用指北
layour: post
uuid: 0c449140-a0ad-11ed-fasfw-e73c5841cd31
tags: [Github]
categories: Github
date: 2024-04-27 18:07:08
---

前几天突发奇想，像是netlify和vercel都是怎么实时获取仓库更新的呢？不可能时每秒钟发送一个get请求到仓库然后获取更新吧。

在经过各位佬的科普后我知道了有WebHook这么一个东西存在。那么根据这个关键词我又在网上进行了一些搜索，在经过一段时间的尝试后，我成功了配置这么一个工具。

首先要确认你需不需要这个工具。在我看来，webhook就是用来获取仓库实时更新然后启动部署网站流程。Vercel和Netlify也确实就是这么一个流程。如果只是想要把网站部署到公网上，选择这两大托管进行部署时不错的选择。如部署到自己的服务器上，配置时必要的。因为我不想每个月都交给Netlify 19 来进行托管，大部分的时间都是浪费这个空间，所以我就想自己部署。
![](https://img.164314.xyz/img/2024/04/73146e52e5a1acdd916837b7dbe85a7c.png)

话不说多，开始教程

# sshKey添加

在对Github进行链接的时候，必须要添加一个sshKey来访问你自己的账户。不然怎么能进行链接你说是吧

## 1.  在服务器上进行对git的全局配置
在双引号中填入你的Github账户名和邮箱。
```
git config --global user.name ""
git config --global user.email ""
```
如成功则会显示你的name和邮箱，如图所示
```
git config --global user.name
git config --global user.email
```
![](https://img.164314.xyz/img/2024/04/0d8177e0acea79bbd9f802600060fc90.png)

## 2. 添加SSH KEY到服务器

```
ssh-keygen -t ed25519 -C "邮箱"
ssh-keygen -t rsa -b 4096 -C "your_email@example.com" // 此命令于上方同价
```
在命令行输入后进行回车一次。输入文件名，此处我使用的文件名叫做githubAcessToken并且我正处于.ssh 文件夹下。如另外保存到别处需输入路径。一路回车最后会出现一个方框（绿色）

![](https://img.164314.xyz/img/2024/04/e17ade635b92c1f38843e488b7959eef.png)

到此我们已经创建了一个名为githubAcessToken和一个githubAcessToken.pub的文件在我的.ssh文件夹下。使用`ls`可以显示出当前目录下所有的文件。

## 3. 复制公钥

`cat githubAcessToken.pub`

使用cat命令可以显示出来公钥，需要复制其内容而后粘贴到git设置中。这里需要复制的公钥不是私钥，不要搞错了。

![](https://img.164314.xyz/img/2024/04/d9277ae1917e9027671a826929f0cb2a.png)

## 4. 粘贴公钥
https://github.com/settings/keys
点击New SSH key粘贴添加即可。这里我已经有三处地方可以用来访问我的github仓库。

![](https://img.164314.xyz/img/2024/04/ccf246e57a119c8c069e164a416e9487.png)

## 测试GIT连接

在服务器中输入
```
ssh -T git@github.com
```
如若访问你的用户名那么即为添加成功。如返回Permission denied那么还需进行下一步测试

`ssh-add githubAcessToken`
![](https://img.164314.xyz/img/2024/04/f6e9fa54ce71f0f66792eca3274bab50.png)

再次进行测试。连接成功
![](https://img.164314.xyz/img/2024/04/83dd4031b1820305c687cc4b1dcb5ef0.png)

## 5. 创建一个空的仓库。

这里不多阐述，直接创建一个空的仓库。进入仓库的serrings-WebHooks-Add webhook
![](https://img.164314.xyz/img/2024/04/83dd4031b1820305c687cc4b1dcb5ef0.png)

## 6. 添加一个新的webHooks

首先需要下载一个插件，进入宝塔的商店，然后搜索，下载，添加到首页
![](https://img.164314.xyz/img/2024/04/a8a5d31c52f0e02703d4af3df33eb295.png)

## 7. WebHook设置

添加一个新的Hook。


![](https://img.164314.xyz/img/2024/04/b10d6809dc72b8732e6e7a64b0e69d6a.png)

![](https://img.164314.xyz/img/2024/04/070e7686ab9a1d57e035e36febcc8fb2.png)

```
#!/bin/bash
echo ""
#输出当前时间
date --date='0 days ago' "+%Y-%m-%d %H:%M:%S"
echo "Start"
#判断宝塔WebHook参数是否存在
if [ ! -n "$1" ];
then 
          echo "param参数错误"
          echo "End"
          exit
fi
#git项目路径（$1是param后面的参数，指向你的服务器的目录）
gitPath="/www/wwwroot/$1"
#git 网址 (替换成你的git地址，ssh方式)
gitHttp="git@github.com:你的账户/仓库名.git"
 
echo "Web站点路径：$gitPath"
 
#判断项目路径是否存在
if [ -d "$gitPath" ]; then
        cd $gitPath
        #判断是否存在git目录
        if [ ! -d ".git" ]; then
                echo "在该目录下克隆 git"
                git clone $gitHttp gittemp
                mv gittemp/.git .
                rm -rf gittemp
        fi
        #拉取最新的项目文件（此处为git拉取命令可根据需求自定义）
        #git reset --hard origin/master
        #git pull origin master
        git fetch --all && git reset --hard origin/master && git pull
        #设置目录权限
        chown -R www:www $gitPath
        echo "End"
        exit
else
        echo "该项目路径不存在"
        echo "End"
        exit
fi
## 感谢以下网上不知名佬提供的这段代码。有太多一样的找不到出处了
```

复制以上代码到Hook设置中进行粘贴，此处只需改更改Github的仓库，直接复制ssh的仓库地址进行粘贴即可。
出现**以下内容**即为添加成功
![](https://img.164314.xyz/img/2024/04/177d6cb1435bbc1c03e79babc9292346.png)


## 8. 添加Hook

回到第五步，复制上一步**查看密钥**里面的链接。打码处为链接
![](https://img.164314.xyz/img/2024/04/177d6cb1435bbc1c03e79babc9292346.png)
类似于以下内容
```
https://服务器IP/hook?access_key=fasfsa&param=aaa
```
注意param后面的aaa需替换为仓库名。

按照我的配置来，然后添加。
当然你也可以选择SSL verification，这里我没有所以就跳过了。
![](https://img.164314.xyz/img/2024/04/a2c061fc06f591a69f36371cb6a6ecd6.png)
 
## 9. 测试

如若一切正常，那么状态码是**200**。

如出现状态码**50x**。将上一步的**ssl**设置为**disable**试试看。

或者需要在服务器中先clone仓库

![](https://img.164314.xyz/img/2024/04/a25a3a2e3ec150c7189dc8950b1e449c.png)

此步为ping测试。接下来我们来进行push测试。

## 10. PUSH测试

首先我在我的服务器中已经clone了仓库。并且使用了`ls`来查看当下仓库下的文件。结果为空因为我还没有上传内容
![](https://img.164314.xyz/img/2024/04/9a58ebb795d157d471bb20e1afd7819f.png)

我现在Github网页版中进行添加一个文件进行测试。我添加了一个`1`
![](https://img.164314.xyz/img/2024/04/f92da9bbeb3d52891a73e48bacd5286e.png)
看一看日志，状态码是200没有错误
![](https://img.164314.xyz/img/2024/04/2994dc5d590713e9b9d685f1391b438b.png)

而后进行服务器目录下查看。一样的结果。到此结束
![](https://img.164314.xyz/img/2024/04/c58a31ed3fcf7664883a5e587453d97f.png)

另外在宝塔插件中日志选项也可以查看
![](https://img.164314.xyz/img/2024/04/5a21d28973bfe3f9e23e81b1afa1d219.png)

另外不要忘记重启以下bt面板

`bt restart`

另外在宝塔插件中日志选项也可以查看
![](https://img.164314.xyz/img/2024/04/5a21d28973bfe3f9e23e81b1afa1d219.png)

另外不要忘记重启以下bt面板

`bt restart`
