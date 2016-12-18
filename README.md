<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgc3f4fc7">1. Python 自学</a>
<ul>
<li><a href="#org9e46aa1">1.1. flask 学习过程中练手代码</a>
<ul>
<li><a href="#org54af8be">1.1.1. mongodb 基本连接</a></li>
<li><a href="#org820a7f7">1.1.2. mySQL 连接</a></li>
</ul>
</li>
<li><a href="#org0845cfb">1.2. python版本相关</a>
<ul>
<li><a href="#org86c0960">1.2.1. virtualenv 下指定python版本</a></li>
</ul>
</li>
<li><a href="#org73ba222">1.3. scrapy初试</a>
<ul>
<li><a href="#org9df4d59">1.3.1. 简单的豆瓣网爬取:tutorial</a></li>
<li><a href="#org428d57a">1.3.2. Meizi网站图片爬取：Meizitu</a></li>
<li><a href="#org19c9fef">1.3.3. Restful Demo</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

<a id="orgc3f4fc7"></a>

# Python 自学


<a id="org9e46aa1"></a>

## flask 学习过程中练手代码


<a id="org54af8be"></a>

### mongodb 基本连接

    运行环境: python3.5
    代码文件夹:mongodb_test  
    lib1(未使用ORM): pymongo, flask_script,  Manager
    lib2(使用ORM): flask_mongoengine, flask_script
    代码:mongodb_test


<a id="org820a7f7"></a>

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


<a id="org0845cfb"></a>

## python版本相关


<a id="org86c0960"></a>

### virtualenv 下指定python版本

    when create virtual environment, using shell command:
    $ virtualenv --python=python2.7 venv
    创建 venv


<a id="org73ba222"></a>

## scrapy初试


<a id="org9df4d59"></a>

### 简单的豆瓣网爬取:tutorial

1.  使用scrapy, python2.7

        $scrapy crawl dmoz  
        在项目主目录下执行


<a id="org428d57a"></a>

### Meizi网站图片爬取：Meizitu

1.  使用scrapy， python2.7, requests

        $ scrapy crawl meizi


<a id="org19c9fef"></a>

### Restful Demo

1.  使用到：flask<sub>restful</sub>, reqparse, abort, Api, Resource

    代码文件夹：restful 

