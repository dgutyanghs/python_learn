<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#org072b755">1. Python 自学</a>
<ul>
<li><a href="#org8f55f7d">1.1. flask 学习过程中练手代码</a>
<ul>
<li><a href="#org188b9be">1.1.1. mongodb 基本连接</a></li>
<li><a href="#org5c56c9e">1.1.2. mySQL 连接</a></li>
<li><a href="#orgea00c25">1.1.3. Restful Demo</a></li>
<li><a href="#org90e4cca">1.1.4. 图片下载 Demo</a></li>
<li><a href="#orgb1ff41a">1.1.5. 图片链接json格式返回</a></li>
</ul>
</li>
<li><a href="#org01fd05e">1.2. python版本相关</a>
<ul>
<li><a href="#orgb3f92b5">1.2.1. virtualenv 下指定python版本</a></li>
</ul>
</li>
<li><a href="#orge27b7ec">1.3. scrapy初试</a>
<ul>
<li><a href="#org6f6a32d">1.3.1. 简单的豆瓣网爬取:tutorial</a></li>
<li><a href="#orgf60a233">1.3.2. Meizi网站图片爬取：Meizitu</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

<a id="org072b755"></a>

# Python 自学


<a id="org8f55f7d"></a>

## flask 学习过程中练手代码


<a id="org188b9be"></a>

### mongodb 基本连接

    运行环境: python3.5
    代码文件夹:mongodb_test  
    lib1(未使用ORM): pymongo, flask_script,  Manager
    lib2(使用ORM): flask_mongoengine, flask_script
    代码:mongodb_test


<a id="org5c56c9e"></a>

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


<a id="orgea00c25"></a>

### Restful Demo

1.  使用到：flask<sub>restful</sub>, reqparse, abort, Api, Resource

    代码文件夹：restful 


<a id="org90e4cca"></a>

### 图片下载 Demo

1.  使用到 request, send<sub>from</sub><sub>directory</sub>, abort ==

        文件夹:picture 
        图片资源:picture/images/*.png
        using this link  to download file http://localhost:5000/images/image2.png


<a id="orgb1ff41a"></a>

### 图片链接json格式返回

1.  flask<sub>restful</sub>, send<sub>from</sub><sub>directory</sub> ==

        代码文件夹：restful -> jsonrestful.py
        图片资源: restful -> images/xxx.jpg ==

2.  WSGI服务器Gunicorn 启动app 命令

        $gunicorn -b 0.0.0.0:8080 yourapp:app

3.  flask返回HTML5的视频

        Browser未能正常播放


<a id="org01fd05e"></a>

## python版本相关


<a id="orgb3f92b5"></a>

### virtualenv 下指定python版本

    when create virtual environment, using shell command:
    $ virtualenv --python=python2.7 venv
    创建 venv


<a id="orge27b7ec"></a>

## scrapy初试


<a id="org6f6a32d"></a>

### 简单的豆瓣网爬取:tutorial

1.  使用scrapy, python2.7

        $scrapy crawl dmoz  
        在项目主目录下执行


<a id="orgf60a233"></a>

### Meizi网站图片爬取：Meizitu

1.  使用scrapy， python2.7, requests

        $ scrapy crawl meizi

