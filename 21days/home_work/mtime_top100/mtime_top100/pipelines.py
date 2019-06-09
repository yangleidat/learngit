# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MtimeTop100Pipeline(object):
    def __init__(self):
        # 初始化要写入的内容
        self.json_file = open('movie_data.json', 'wb+')
        self.json_file.write('\n'.encode('utf-8'))
        

    # 该方法中的item就是爬虫中的item
    def process_item(self, item, spider):
        # return item
        # print('电影名称', item['movie_name'])
        # print('导演', item['director'])
        # print('评分', item['score'])
        text = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.json_file.write(text.encode('utf-8'))

    # 当爬虫关闭的时候，程序要关闭文件
    def close_spider(self, spider):
        print('-----------关闭文件--------------')
        #退2个字节
        self.json_file.seek(-2, 1)
        self.json_file.write('\n'.encode('utf-8'))
        self.json_file.close()