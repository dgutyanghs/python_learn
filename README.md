<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#org6c2a361">1. Python 自学</a>
<ul>
<li><a href="#org2634055">1.1. flask 学习过程中练手代码</a>
<ul>
<li><a href="#orgeab58d2">1.1.1. mongodb 基本连接</a></li>
<li><a href="#orgd85fce1">1.1.2. mySQL 连接</a></li>
<li><a href="#org3bc3d7f">1.1.3. Restful Demo</a></li>
<li><a href="#org715e1dc">1.1.4. 图片下载 Demo</a></li>
<li><a href="#org58d90a4">1.1.5. 图片链接json格式返回</a></li>
</ul>
</li>
<li><a href="#org9902371">1.2. python版本相关</a>
<ul>
<li><a href="#org80e7821">1.2.1. virtualenv 下指定python版本</a></li>
</ul>
</li>
<li><a href="#org266ee12">1.3. scrapy初试</a>
<ul>
<li><a href="#orgbcb5720">1.3.1. 简单的豆瓣网爬取:tutorial</a></li>
<li><a href="#orga78c55c">1.3.2. Meizi网站图片爬取：Meizitu</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

<a id="org6c2a361"></a>

# Python 自学


<a id="org2634055"></a>

## flask 学习过程中练手代码


<a id="orgeab58d2"></a>

### mongodb 基本连接

    运行环境: python3.5
    代码文件夹:mongodb_test  
    lib1(未使用ORM): pymongo, flask_script,  Manager
    lib2(使用ORM): flask_mongoengine, flask_script
    代码:mongodb_test


<a id="orgd85fce1"></a>

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

4.  mySQL 的ORM

        mysql_test 目录下： app.py, manager.py, modules.py 
        >>>python manager save
        ...
        >>> python manager query_all


<a id="org3bc3d7f"></a>

### Restful Demo

1.  使用到：flask<sub>restful</sub>, reqparse, abort, Api, Resource

    代码文件夹：restful 


<a id="org715e1dc"></a>

### 图片下载 Demo

1.  使用到 request, send<sub>from</sub><sub>directory</sub>, abort ==

        文件夹:picture 
        图片资源:picture/images/*.png
        using this link  to download file http://localhost:5000/images/image2.png


<a id="org58d90a4"></a>

### 图片链接json格式返回

1.  flask<sub>restful</sub>, send<sub>from</sub><sub>directory</sub> ==

        代码文件夹：restful -> jsonrestful.py
        图片资源: restful -> images/xxx.jpg ==


<a id="org9902371"></a>

## python版本相关


<a id="org80e7821"></a>

### virtualenv 下指定python版本

    when create virtual environment, using shell command:
    $ virtualenv --python=python2.7 venv
    创建 venv


<a id="org266ee12"></a>

## scrapy初试


<a id="orgbcb5720"></a>

### 简单的豆瓣网爬取:tutorial

1.  使用scrapy, python2.7

        $scrapy crawl dmoz  
        在项目主目录下执行


<a id="orga78c55c"></a>

### Meizi网站图片爬取：Meizitu

1.  使用scrapy， python2.7, requests

        $ scrapy crawl meizi

