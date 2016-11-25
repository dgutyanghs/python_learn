<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#orgheadline11">1. Python 自学</a>
<ul>
<li><a href="#orgheadline5">1.1. flask 学习过程中练手代码</a>
<ul>
<li><a href="#orgheadline1">1.1.1. mongodb 基本连接</a></li>
<li><a href="#orgheadline4">1.1.2. mySQL 连接</a></li>
</ul>
</li>
<li><a href="#orgheadline7">1.2. python版本相关</a>
<ul>
<li><a href="#orgheadline6">1.2.1. virtualenv 下指定python版本</a></li>
</ul>
</li>
<li><a href="#orgheadline10">1.3. scrapy初试</a>
<ul>
<li><a href="#orgheadline9">1.3.1. 简单的豆瓣网爬取:tutorial</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

# Python 自学<a id="orgheadline11"></a>

## flask 学习过程中练手代码<a id="orgheadline5"></a>

### mongodb 基本连接<a id="orgheadline1"></a>

    运行环境: python3.5
    代码文件夹:mongodb_test  
    lib1(未使用ORM): pymongo, flask_script,  Manager
    lib2(使用ORM): flask_mongoengine, flask_script
    代码:mongodb_test

### mySQL 连接<a id="orgheadline4"></a>

1.  mySQL 服务器启动命令

        $ mysql.server start
        $ mysql.server stop
        $ mysql.server restart

2.  mySQL 连接服务器

          $ mysql -u root -p
        if have password , then enter....
          $ yourpassword

## python版本相关<a id="orgheadline7"></a>

### virtualenv 下指定python版本<a id="orgheadline6"></a>

    when create virtual environment, using shell command:
    $ virtualenv --python=python2.7 venv
    创建 venv

## scrapy初试<a id="orgheadline10"></a>

### 简单的豆瓣网爬取:tutorial<a id="orgheadline9"></a>

1.  使用scrapy, python2.7

        $scrapy crawl dmoz  
        在项目主目录下执行
