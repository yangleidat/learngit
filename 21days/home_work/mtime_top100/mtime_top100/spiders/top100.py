# -*- coding: utf-8 -*-
import scrapy
from mtime_top100.items import MtimeTop100Item

class Top100Spider(scrapy.Spider):
    # 爬虫的名字
    name = 'top100'
    # 爬取的域名
    allowed_domains = ['www.mtime.com']
    # 从哪个页面开始爬取
    start_urls = ['http://www.mtime.com/top/movie/top100/']

    # 该response就代表scrapy下载器所获取的目标的响应
    # 和shell调试中的response对象完全一样
    def parse(self, response):
        item = MtimeTop100Item()
        
        # 每个movie包含一个电影的信息
        for movie in response.xpath('//*[@class="top_list"]/ul/li'):
            item['number'] = movie.xpath('./div[@class="number"]/em/text()').extract_first()
            item['movie_name'] = movie.xpath('./div[@class="mov_con"]/h2/a/text()').extract_first()
            item['director'] = movie.xpath('./div[@class="mov_con"]/p/a/text()').extract_first()
            point = movie.xpath('./div[@class="mov_point"]/b/span/text()').extract()
            if point and len(point) > 1:
                item['score'] = point[0]+point[1]
            
            yield item
        for page_index in range(2,11):    
            new_link = 'http://www.mtime.com/top/movie/top100/index-{}.html'.format(page_index)
            yield scrapy.Request(new_link, callback=self.parse)