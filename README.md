<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#org8cc2a7d">1. Python 自学</a>
<ul>
<li><a href="#org82067a8">1.1. flask 学习过程中练手代码</a>
<ul>
<li><a href="#org8fd7f2e">1.1.1. mongodb 基本连接</a></li>
<li><a href="#org265a01b">1.1.2. mySQL 连接</a></li>
<li><a href="#org8f98f31">1.1.3. Restful Demo</a></li>
<li><a href="#orgbf8bac3">1.1.4. 图片下载 Demo</a></li>
<li><a href="#org9a1483a">1.1.5. 图片链接json格式返回</a></li>
</ul>
</li>
<li><a href="#org204e2e2">1.2. python版本相关</a>
<ul>
<li><a href="#org9b3bf09">1.2.1. virtualenv 下指定python版本</a></li>
</ul>
</li>
<li><a href="#orgd4550e2">1.3. scrapy初试</a>
<ul>
<li><a href="#orgb453515">1.3.1. 简单的豆瓣网爬取:tutorial</a></li>
<li><a href="#orgf2decb0">1.3.2. Meizi网站图片爬取：Meizitu</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

<a id="org8cc2a7d"></a>

# Python 自学


<a id="org82067a8"></a>

## flask 学习过程中练手代码


<a id="org8fd7f2e"></a>

### mongodb 基本连接

    运行环境: python3.5
    代码文件夹:mongodb_test  
    lib1(未使用ORM): pymongo, flask_script,  Manager
    lib2(使用ORM): flask_mongoengine, flask_script
    代码:mongodb_test 


<a id="org265a01b"></a>

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

6.  SqlAlchemy query 结果排序 desc

        class Hotnews(Resource):
            def get(self):
                from models import Pianonews
                return jsonify(pianonews = [item.serialize for item in Pianonews.query.order_by(desc(Pianonews.index))])
                #return jsonify(pianonews = [item.serialize for item in Pianonews.query.all()]) 
        
        
            def post(self):
                from models import Pianonews
                return jsonify(pianonews = [item.serialize for item in Pianonews.query.all()])
    
    见 restful app.py文件

7.  Mysql 更改表的Auto increment

        > ALTER TABLE `videoslist` CHANGE COLUMN `index` `index` INT(4) NOT NULL AUTO_INCREMENT;
        
        or
        > ALTER TABLE  `videoslist` ADD  `index` INT( 11 ) NOT NULL  PRIMARY KEY AUTO_INCREMENT FIRST
        注意` ` 不是' '号

8.  MySQL 的table名字区分大小写

    可用下面SQL更改表名
    
        $: RENAME TABLE old_table TO new_table;

9.  MySQL 创建Table

        CREATE TABLE `videoslisttest` (
          `index` int(11) NOT NULL AUTO_INCREMENT,
          `title` varchar(255) DEFAULT NULL,
          `cover` varchar(255) DEFAULT NULL,
          `mp4_url` varchar(255) DEFAULT NULL,
          `desc` varchar(1000) DEFAULT NULL,
          PRIMARY KEY (`index`)
        ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;


<a id="org8f98f31"></a>

### Restful Demo

1.  使用到：flask<sub>restful</sub>, reqparse, abort, Api, Resource

    代码文件夹：restful 


<a id="orgbf8bac3"></a>

### 图片下载 Demo

1.  使用到 request, send<sub>from</sub><sub>directory</sub>, abort ==

        文件夹:picture 
        图片资源:picture/images/*.png
        using this link  to download file http://localhost:5000/images/image2.png


<a id="org9a1483a"></a>

### 图片链接json格式返回

1.  flask<sub>restful</sub>, send<sub>from</sub><sub>directory</sub> ==

        代码文件夹：restful -> jsonrestful.py
        图片资源: restful -> images/xxx.jpg ==

2.  WSGI服务器Gunicorn 启动app 命令

        $gunicorn -b 0.0.0.0:8080 yourapp:app

3.  flask返回HTML5的视频

        Browser未能正常播放


<a id="org204e2e2"></a>

## python版本相关


<a id="org9b3bf09"></a>

### virtualenv 下指定python版本

    
    $ sudo apt-get install python-pip
    $ sudo apt-get install python-virtualenv

    when create virtual environment, using shell command:
    $ virtualenv --python=python2.7 venv
    创建 venv

    # //默认情况下，虚拟环境会依赖系统环境中的site packages，
    #就是说系统中已经安装好的第三方package也会安装在虚拟环境中，如果不想依赖这些package，那么可以加上参数 --no-site-packages建立虚拟环境
    $ virtualenv --no-site-package venv


<a id="orgd4550e2"></a>

## scrapy初试


<a id="orgb453515"></a>

### 简单的豆瓣网爬取:tutorial

1.  使用scrapy, python2.7

        $scrapy crawl dmoz  
        在项目主目录下执行 


<a id="orgf2decb0"></a>

### Meizi网站图片爬取：Meizitu

1.  使用scrapy， python2.7, requests

        $ scrapy crawl meizi

