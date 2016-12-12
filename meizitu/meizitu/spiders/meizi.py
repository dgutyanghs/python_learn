# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
#Item Loaders提供了一种便捷的方式填充抓取到的 :Items
# from scrapy.contrib.loader import ItemLoader, Identity
from scrapy.loader import ItemLoader, Identity
from meizitu.items import MeizituItem
import pdb

class MeiziSpider(scrapy.Spider):
    name = "meizi"
    allowed_domains = ["meizitu.com"]
    start_urls = (
        # 'http://www.meizitu.com/',
        # 'http://www.meizitu.com/a/list_1_87.html', 
        'http://www.meizitu.com/a/xinggan.html',
    )

    def parse(self, response):
        #sel是页面源代码，载入scrapy.selector
        sel = Selector(response)
        #每个连接，用@href属性
        for link in sel.xpath('//h3/a/@href').extract():
            #请求=Request(连接，parese_item)
            # pdb.set_trace() 
            # pdb.test()
            request = scrapy.Request(link, callback=self.parse_item)
            yield request#返回请求
        #获取页码集合
        # pages = sel.xpath('//*[@id="wp_page_numbers"]/ul/li/a/@href').extract()
        # # print('pages: %s' % pages)#打印页码
        # if len(pages) > 2:#如果页码集合>2
        #     page_link = pages[-2]#图片连接=读取页码集合的倒数第二个页码
        #     page_link = page_link.replace('/a/', '')#图片连接=page_link（a替换成空）
        #     # print('page_link %s', page_link)
        #     request = scrapy.Request('http://www.meizitu.com/a/%s' % page_link, callback=self.parse)
        #     yield request#返回请求

    def parse_item(self, response):
        #l=用ItemLoader载入MeizituItem()
        l = ItemLoader(item=MeizituItem(), response=response)
        #名字
        l.add_xpath('name', '//h2/a/text()')
        #标签
        l.add_xpath('tags', "//div[@id='maincontent']/div[@class='postmeta  clearfix']/div[@class='metaRight']/p")
        #图片连接
        l.add_xpath('image_urls', "//div[@id='picture']/p/img/@src", Identity())
        # print("response.url %s" %response.url)
        # pdb.test()
        # l.add_value('url', response.url)
        return l.load_item()

