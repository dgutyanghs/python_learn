<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline18">1. Python 自学</a>
<ul>
<li><a href="#orgheadline10">1.1. flask 学习过程中练手代码</a>
<ul>
<li><a href="#orgheadline1">1.1.1. mongodb 基本连接</a></li>
<li><a href="#orgheadline5">1.1.2. mySQL 连接</a></li>
<li><a href="#orgheadline7">1.1.3. Restful Demo</a></li>
<li><a href="#orgheadline9">1.1.4. 图片下载 Demo</a></li>
</ul>
</li>
<li><a href="#orgheadline12">1.2. python版本相关</a>
<ul>
<li><a href="#orgheadline11">1.2.1. virtualenv 下指定python版本</a></li>
</ul>
</li>
<li><a href="#orgheadline17">1.3. scrapy初试</a>
<ul>
<li><a href="#orgheadline14">1.3.1. 简单的豆瓣网爬取:tutorial</a></li>
<li><a href="#orgheadline16">1.3.2. Meizi网站图片爬取：Meizitu</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

# Python 自学<a id="orgheadline18"></a>

## flask 学习过程中练手代码<a id="orgheadline10"></a>

### mongodb 基本连接<a id="orgheadline1"></a>

    运行环境: python3.5
    代码文件夹:mongodb_test  
    lib1(未使用ORM): pymongo, flask_script,  Manager
    lib2(使用ORM): flask_mongoengine, flask_script
    代码:mongodb_test

### mySQL 连接<a id="orgheadline5"></a>

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

### Restful Demo<a id="orgheadline7"></a>

1.  使用到：flask<sub>restful</sub>, reqparse, abort, Api, Resource

    代码文件夹：restful 

### 图片下载 Demo<a id="orgheadline9"></a>

1.  使用到 request, send<sub>from</sub><sub>directory</sub>, abort ==

        文件夹:picture 
        图片资源:picture/images/*.png
        using this link  to download file http://localhost:5000/images/image2.png

## python版本相关<a id="orgheadline12"></a>

### virtualenv 下指定python版本<a id="orgheadline11"></a>

    when create virtual environment, using shell command:
    $ virtualenv --python=python2.7 venv
    创建 venv

## scrapy初试<a id="orgheadline17"></a>

### 简单的豆瓣网爬取:tutorial<a id="orgheadline14"></a>

1.  使用scrapy, python2.7

        $scrapy crawl dmoz  
        在项目主目录下执行

### Meizi网站图片爬取：Meizitu<a id="orgheadline16"></a>

1.  使用scrapy， python2.7, requests

        $ scrapy crawl meizi
