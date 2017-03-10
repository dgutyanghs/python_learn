<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgeaa0139">1. Python 自学</a>
<ul>
<li><a href="#org63615b7">1.1. flask 学习过程中练手代码</a>
<ul>
<li><a href="#org8366742">1.1.1. mongodb 基本连接</a></li>
<li><a href="#orgf9c686e">1.1.2. mySQL 连接</a></li>
<li><a href="#org05c95ac">1.1.3. Restful Demo</a></li>
<li><a href="#orgfeb99da">1.1.4. 图片下载 Demo</a></li>
<li><a href="#orga4f3ee4">1.1.5. 图片链接json格式返回</a></li>
</ul>
</li>
<li><a href="#orgba4feff">1.2. python版本相关</a>
<ul>
<li><a href="#orgfd809fc">1.2.1. virtualenv 下指定python版本</a></li>
</ul>
</li>
<li><a href="#orga3407e4">1.3. scrapy初试</a>
<ul>
<li><a href="#org9779e4b">1.3.1. 简单的豆瓣网爬取:tutorial</a></li>
<li><a href="#orgb315f69">1.3.2. Meizi网站图片爬取：Meizitu</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

<a id="orgeaa0139"></a>

# Python 自学


<a id="org63615b7"></a>

## flask 学习过程中练手代码


<a id="org8366742"></a>

### mongodb 基本连接

    运行环境: python3.5
    代码文件夹:mongodb_test  
    lib1(未使用ORM): pymongo, flask_script,  Manager
    lib2(使用ORM): flask_mongoengine, flask_script
    代码:mongodb_test


<a id="orgf9c686e"></a>

### mySQL 连接

1.  mySQL 服务器启动命令

        $ mysql.server start
        $ mysql.server stop
        $ mysql.server restart

2.  mySQL 连接服务器

          $ mysql -u root -p
        if have password , then enter....
          $ yourpassword

3.  Change MySQL password

        mysql> SET PASSWORD FOR 'tom'@'localhost' = PASSWORD('foobar');
        mysql> FLUSH PRIVILEGES;
        mysql> quit;
        
        $ mysql -u tom -p
        $ yourpassword
        
        then login ok

4.  mySQL 的ORM, json serialize

        mysql_test 目录下： app.py, manager.py, modules.py 
        >>>python manager save
        ...
        >>> python manager query_all

5.  MySQL 中文乱码的solution

        CREATE DATABASE mydb
          DEFAULT CHARACTER SET utf8
          DEFAULT COLLATE utf8_general_ci;


<a id="org05c95ac"></a>

### Restful Demo

1.  使用到：flask<sub>restful</sub>, reqparse, abort, Api, Resource

    代码文件夹：restful 


<a id="orgfeb99da"></a>

### 图片下载 Demo

1.  使用到 request, send<sub>from</sub><sub>directory</sub>, abort ==

        文件夹:picture 
        图片资源:picture/images/*.png
        using this link  to download file http://localhost:5000/images/image2.png


<a id="orga4f3ee4"></a>

### 图片链接json格式返回

1.  flask<sub>restful</sub>, send<sub>from</sub><sub>directory</sub> ==

        代码文件夹：restful -> jsonrestful.py
        图片资源: restful -> images/xxx.jpg ==

2.  WSGI服务器Gunicorn 启动app 命令

        $gunicorn -b 0.0.0.0:8080 yourapp:app

3.  flask返回HTML5的视频

        Browser未能正常播放


<a id="orgba4feff"></a>

## python版本相关


<a id="orgfd809fc"></a>

### virtualenv 下指定python版本

    when create virtual environment, using shell command:
    $ virtualenv --python=python2.7 venv
    创建 venv


<a id="orga3407e4"></a>

## scrapy初试


<a id="org9779e4b"></a>

### 简单的豆瓣网爬取:tutorial

1.  使用scrapy, python2.7

        $scrapy crawl dmoz  
        在项目主目录下执行


<a id="orgb315f69"></a>

### Meizi网站图片爬取：Meizitu

1.  使用scrapy， python2.7, requests

        $ scrapy crawl meizi

