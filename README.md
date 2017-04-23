<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#org86aa045">1. Python 自学</a>
<ul>
<li><a href="#orge01ef35">1.1. flask 学习过程中练手代码</a>
<ul>
<li><a href="#org781d415">1.1.1. mongodb 基本连接</a></li>
<li><a href="#org8187295">1.1.2. mySQL 连接</a></li>
<li><a href="#org4cc6d1e">1.1.3. Restful Demo</a></li>
<li><a href="#org2313dc3">1.1.4. 图片下载 Demo</a></li>
<li><a href="#org7efcb94">1.1.5. 图片链接json格式返回</a></li>
</ul>
</li>
<li><a href="#orga4a5dfe">1.2. python版本相关</a>
<ul>
<li><a href="#org3f4564c">1.2.1. virtualenv 下指定python版本</a></li>
</ul>
</li>
<li><a href="#orgb54339c">1.3. scrapy初试</a>
<ul>
<li><a href="#orgc9840d3">1.3.1. 简单的豆瓣网爬取:tutorial</a></li>
<li><a href="#org8b17cc9">1.3.2. Meizi网站图片爬取：Meizitu</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

<a id="org86aa045"></a>

# Python 自学


<a id="orge01ef35"></a>

## flask 学习过程中练手代码


<a id="org781d415"></a>

### mongodb 基本连接

    运行环境: python3.5
    代码文件夹:mongodb_test  
    lib1(未使用ORM): pymongo, flask_script,  Manager
    lib2(使用ORM): flask_mongoengine, flask_script
    代码:mongodb_test


<a id="org8187295"></a>

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


<a id="org4cc6d1e"></a>

### Restful Demo

1.  使用到：flask<sub>restful</sub>, reqparse, abort, Api, Resource

    代码文件夹：restful 


<a id="org2313dc3"></a>

### 图片下载 Demo

1.  使用到 request, send<sub>from</sub><sub>directory</sub>, abort ==

        文件夹:picture 
        图片资源:picture/images/*.png
        using this link  to download file http://localhost:5000/images/image2.png


<a id="org7efcb94"></a>

### 图片链接json格式返回

1.  flask<sub>restful</sub>, send<sub>from</sub><sub>directory</sub> ==

        代码文件夹：restful -> jsonrestful.py
        图片资源: restful -> images/xxx.jpg ==

2.  WSGI服务器Gunicorn 启动app 命令

        $gunicorn -b 0.0.0.0:8080 yourapp:app

3.  flask返回HTML5的视频

        Browser未能正常播放


<a id="orga4a5dfe"></a>

## python版本相关


<a id="org3f4564c"></a>

### virtualenv 下指定python版本

    when create virtual environment, using shell command:
    $ virtualenv --python=python2.7 venv
    创建 venv


<a id="orgb54339c"></a>

## scrapy初试


<a id="orgc9840d3"></a>

### 简单的豆瓣网爬取:tutorial

1.  使用scrapy, python2.7

        $scrapy crawl dmoz  
        在项目主目录下执行


<a id="org8b17cc9"></a>

### Meizi网站图片爬取：Meizitu

1.  使用scrapy， python2.7, requests

        $ scrapy crawl meizi

