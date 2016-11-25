import  scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        # "http://www.smartcoach.cn:8081/",
        # "https://www.smartcoach.cn:8082/",
        # "https://site.douban.com/mmt/widget/notes/190578992/note/576867955/",
        "https://site.douban.com/mmt/widget/notes/190578992/?start=0",
        "https://site.douban.com/mmt/widget/notes/190578992/?start=10",
        "https://site.douban.com/mmt/widget/notes/190578992/?start=20",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        # "http://news.piano-china.com/sort/4.html",
        # "https://s.taobao.com/search?q=kawai&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.50862.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20161125"
    ]


    # def parse(self, response):
    #     filename = response.url.split("/")[-2] + '.html'
    #     str_name = "!! (%s)" %(filename)
    #     print (str_name)
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)


    # def parse(self, response):
    #     for sel in response.xpath('//ul/li'):
    #         title = sel.xpath('a/text()').extract()
    #         link = sel.xpath('a/@href').extract()
    #         desc = sel.xpath('text()').extract()
    #         print title, link, desc

    # def parse(self, response):
    #     for sel in response.xpath('//ul/li'):
    #         item = DmozItem()
    #         item['title'] = sel.xpath('a/text()').extract()
    #         item['link'] = sel.xpath('a/@href').extract()
    #         item['desc'] = sel.xpath('text()').extract()
    #         yield item


    def parse(self, response):
        # for sel in response.xpath('//li/a/text()').extract():
        for sel in response.xpath('//h3/a/text()').extract():
        # for sel in response.xpath('//div/h1/text()').extract():
        # for sel in response.xpath('//span/a/text()').extract():
        # for sel in response.xpath('//div/a/text()').extract():
            print sel






