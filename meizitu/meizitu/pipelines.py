# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class MeizituPipeline(object):
#     def process_item(self, item, spider):
#         return item

import requests
from meizitu import settings
import os

#图片下载类
class MeizituPipeline(object):
    def process_item(self, item, spider):
        if 'image_urls' in item:#如何‘图片地址’在项目中
            images = []#定义图片空集
            
            dir_path = '%s/%s' % (settings.IMAGES_STORE, spider.name)

            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            # images = ['http://img4.cache.netease.com/photo/0008/2016-12-12/C828MC072FKJ0008.550x.0.jpg', 'http://mm.howkuai.com/wp-content/uploads/2016a/09/02/01.jpg']
            for image_url in item['image_urls']:
            # for image_url in images:
                us = image_url.split('/')[3:]
                image_file_name = '_'.join(us)
                file_path = '%s/%s' % (dir_path, image_file_name)
                images.append(file_path)
                if os.path.exists(file_path):
                    continue

                with open(file_path, 'wb') as handle:
                    print("image_url:%s"%image_url)
                    response = requests.get(image_url, stream=True)
                    for block in response.iter_content(chunk_size = 1024):
                        if not block:
                            print('download break %s'%len(block))
                            break
                        
                        # print('download ok %s'%len(block))
                        handle.write(block)

            item['images'] = images

        return item
