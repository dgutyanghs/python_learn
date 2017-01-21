<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#org127d051">1. Python 自学</a>
<ul>
<li><a href="#orgaa71ef6">1.1. flask 学习过程中练手代码</a>
<ul>
<li><a href="#org2efe018">1.1.1. mongodb 基本连接</a></li>
<li><a href="#org8aaca1d">1.1.2. mySQL 连接</a></li>
<li><a href="#org4babd15">1.1.3. Restful Demo</a></li>
<li><a href="#org964211b">1.1.4. 图片下载 Demo</a></li>
<li><a href="#org32d3022">1.1.5. 图片链接json格式返回</a></li>
</ul>
</li>
<li><a href="#orgc330bd6">1.2. python版本相关</a>
<ul>
<li><a href="#orgd67a8fe">1.2.1. virtualenv 下指定python版本</a></li>
</ul>
</li>
<li><a href="#orgd782f9f">1.3. scrapy初试</a>
<ul>
<li><a href="#org16789ab">1.3.1. 简单的豆瓣网爬取:tutorial</a></li>
<li><a href="#orgb985c98">1.3.2. Meizi网站图片爬取：Meizitu</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

<a id="org127d051"></a>

# Python 自学


<a id="orgaa71ef6"></a>

## flask 学习过程中练手代码


<a id="org2efe018"></a>

### mongodb 基本连接

    运行环境: python3.5
    代码文件夹:mongodb_test  
    lib1(未使用ORM): pymongo, flask_script,  Manager
    lib2(使用ORM): flask_mongoengine, flask_script
    代码:mongodb_test


<a id="org8aaca1d"></a>

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

    \#+BEGIN<sub>SRC</sub> sql
    mysql> SET PASSWORD FOR 'tom'@'localhost' = PASSWORD('foobar');
    mysql> FLUSH PRIVILEGES;
    mysql> quit;
    
    $ mysql -u tom -p
    $ yourpassword
    
    then login ok
    
    \#+END<sub>SR</sub>

4.  mySQL 的ORM, json serialize

        mysql_test 目录下： app.py, manager.py, modules.py 
        >>>python manager save
        ...
        >>> python manager query_all

5.  MySQL 中文乱码的solution

        CREATE DATABASE mydb
          DEFAULT CHARACTER SET utf8
          DEFAULT COLLATE utf8_general_ci;


<a id="org4babd15"></a>

### Restful Demo

1.  使用到：flask<sub>restful</sub>, reqparse, abort, Api, Resource

    代码文件夹：restful 


<a id="org964211b"></a>

### 图片下载 Demo

1.  使用到 request, send<sub>from</sub><sub>directory</sub>, abort ==

        文件夹:picture 
        图片资源:picture/images/*.png
        using this link  to download file http://localhost:5000/images/image2.png


<a id="org32d3022"></a>

### 图片链接json格式返回

1.  flask<sub>restful</sub>, send<sub>from</sub><sub>directory</sub> ==

        代码文件夹：restful -> jsonrestful.py
        图片资源: restful -> images/xxx.jpg ==


<a id="orgc330bd6"></a>

## python版本相关


<a id="orgd67a8fe"></a>

### virtualenv 下指定python版本

    when create virtual environment, using shell command:
    $ virtualenv --python=python2.7 venv
    创建 venv


<a id="orgd782f9f"></a>

## scrapy初试


<a id="org16789ab"></a>

### 简单的豆瓣网爬取:tutorial

1.  使用scrapy, python2.7

        $scrapy crawl dmoz  
        在项目主目录下执行


<a id="orgb985c98"></a>

### Meizi网站图片爬取：Meizitu

1.  使用scrapy， python2.7, requests

        $ scrapy crawl meizi

