<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#org8dc3b15">1. Python 自学</a>
<ul>
<li><a href="#orgea0be60">1.1. flask 学习过程中练手代码</a>
<ul>
<li><a href="#org44ffaba">1.1.1. mongodb 基本连接</a></li>
<li><a href="#orgb88fb52">1.1.2. mySQL 连接</a></li>
</ul>
</li>
<li><a href="#org6ac71f5">1.2. python版本相关</a>
<ul>
<li><a href="#orgb0b3973">1.2.1. virtualenv 下指定python版本</a></li>
</ul>
</li>
<li><a href="#org4de5027">1.3. scrapy初试</a>
<ul>
<li><a href="#orgcc561d9">1.3.1. 简单的豆瓣网爬取:tutorial</a></li>
<li><a href="#org65af4d8">1.3.2. Meizi网站图片爬取：Meizitu</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

<a id="org8dc3b15"></a>

# Python 自学


<a id="orgea0be60"></a>

## flask 学习过程中练手代码


<a id="org44ffaba"></a>

### mongodb 基本连接

    运行环境: python3.5
    代码文件夹:mongodb_test  
    lib1(未使用ORM): pymongo, flask_script,  Manager
    lib2(使用ORM): flask_mongoengine, flask_script
    代码:mongodb_test


<a id="orgb88fb52"></a>

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


<a id="org6ac71f5"></a>

## python版本相关


<a id="orgb0b3973"></a>

### virtualenv 下指定python版本

    when create virtual environment, using shell command:
    $ virtualenv --python=python2.7 venv
    创建 venv


<a id="org4de5027"></a>

## scrapy初试


<a id="orgcc561d9"></a>

### 简单的豆瓣网爬取:tutorial

1.  使用scrapy, python2.7

        $scrapy crawl dmoz  
        在项目主目录下执行


<a id="org65af4d8"></a>

### Meizi网站图片爬取：Meizitu

1.  使用scrapy， python2.7, requests

        $ scrapy crawl meizi

