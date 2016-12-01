
# -*- coding:utf-8 -*-

import  scrapy

# from popiano.items import PopianoItem
from urlparse import urljoin
from popianotest.items import PopianotestItem


class Popiano(scrapy.Spider):
    name = "popianotest1"
    allowed_domains = ["www.popiano.org"]
    start_urls = [
        "http://bbs.popiano.org/forum.php?mod=guide",
        "http://bbs.popiano.org/forum.php?mod=guide&view=hot&page=2"
    ]


    def parse(self, response):
        links = response.xpath('//th[contains(@class,"common")]/a/@href').extract()
        i = 0
        for link in links:
            item = PopianotestItem()
            full_link = urljoin(response.url, link)
            print full_link
            item['link'] = full_link
            i += 1
            item['link_num'] = i
            yield item 




# <html>
#  <head>
#   <base href='http://example.com/' />
#   <title>Example website</title>
#  </head>
#  <body>
#   <div id='images'>
#    <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>
#    <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>
#    <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>
#    <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>
#    <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>
#   </div>
#  </body>
# </html>
