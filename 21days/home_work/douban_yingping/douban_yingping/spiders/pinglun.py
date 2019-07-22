# -*- coding: utf-8 -*-
import scrapy
from douban_yingping.items import DoubanYingpingItem
import time


class PinglunSpider(scrapy.Spider):
    name = 'pinglun'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/subject/27200988/comments?status=P']

    def parse(self, response):
        item = DoubanYingpingItem()

        for duanping in response.xpath('//*[@id="comments"]/div'):
            time.sleep(0.2)
            item['user_id'] = duanping.xpath('./div[2]/h3/span[2]/a/text()').extract_first()
            item['stars'] = duanping.xpath('./div[2]/h3/span[2]/span[2]/@title').extract_first()
            item['date'] = duanping.xpath('./div[2]/h3/span[2]/span[3]/@title').extract_first()
            item['good'] = duanping.xpath('./div[2]/h3/span[1]/span/text()').extract_first()
            item['all_text'] = duanping.xpath('./div[2]/p/span/text()').extract_first()
            yield item

        for next_pages in response.xpath('//*[@id="paginator"]/a'):
            if '后页' in next_pages.xpath('./text()').extract_first():
                new_link = 'https://movie.douban.com/subject/27200988/comments'+next_pages.xpath('./@href').extract_first().replace('&percent_type=','')
                yield scrapy.Request(new_link, callback=self.parse)