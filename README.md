<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#org9bb4096">1. Python 自学</a>
<ul>
<li><a href="#org1c6cf99">1.1. flask 学习过程中练手代码</a>
<ul>
<li><a href="#org8533fa4">1.1.1. mongodb 基本连接</a></li>
<li><a href="#orgcbb59dc">1.1.2. mySQL 连接</a></li>
<li><a href="#orga3cdaad">1.1.3. Restful Demo</a></li>
<li><a href="#org1ea33d6">1.1.4. 图片下载 Demo</a></li>
<li><a href="#org7382300">1.1.5. 图片链接json格式返回</a></li>
</ul>
</li>
<li><a href="#orga390cdb">1.2. python版本相关</a>
<ul>
<li><a href="#org5cd6409">1.2.1. virtualenv 下指定python版本</a></li>
</ul>
</li>
<li><a href="#org8cb2bac">1.3. scrapy初试</a>
<ul>
<li><a href="#org9edbb1c">1.3.1. 简单的豆瓣网爬取:tutorial</a></li>
<li><a href="#org88b642e">1.3.2. Meizi网站图片爬取：Meizitu</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

<a id="org9bb4096"></a>

# Python 自学


<a id="org1c6cf99"></a>

## flask 学习过程中练手代码


<a id="org8533fa4"></a>

### mongodb 基本连接

    运行环境: python3.5
    代码文件夹:mongodb_test  
    lib1(未使用ORM): pymongo, flask_script,  Manager
    lib2(使用ORM): flask_mongoengine, flask_script
    代码:mongodb_test


<a id="orgcbb59dc"></a>

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


<a id="orga3cdaad"></a>

### Restful Demo

1.  使用到：flask<sub>restful</sub>, reqparse, abort, Api, Resource

    代码文件夹：restful 


<a id="org1ea33d6"></a>

### 图片下载 Demo

1.  使用到 request, send<sub>from</sub><sub>directory</sub>, abort ==

        文件夹:picture 
        图片资源:picture/images/*.png
        using this link  to download file http://localhost:5000/images/image2.png


<a id="org7382300"></a>

### 图片链接json格式返回

1.  flask<sub>restful</sub>, send<sub>from</sub><sub>directory</sub> ==

        代码文件夹：restful -> jsonrestful.py
        图片资源: restful -> images/xxx.jpg ==


<a id="orga390cdb"></a>

## python版本相关


<a id="org5cd6409"></a>

### virtualenv 下指定python版本

    when create virtual environment, using shell command:
    $ virtualenv --python=python2.7 venv
    创建 venv


<a id="org8cb2bac"></a>

## scrapy初试


<a id="org9edbb1c"></a>

### 简单的豆瓣网爬取:tutorial

1.  使用scrapy, python2.7

        $scrapy crawl dmoz  
        在项目主目录下执行


<a id="org88b642e"></a>

### Meizi网站图片爬取：Meizitu

1.  使用scrapy， python2.7, requests

        $ scrapy crawl meizi

