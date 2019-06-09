# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MtimeTop100Item(scrapy.Item):
    # define the fields for your item here like:
    # 电影名称
    movie_name = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 排名
    number = scrapy.Field()
