# -*- coding: utf-8 -*-
import scrapy
from dd.items import DdItem
from scrapy.http import Request
class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.54.06.19.00.00.html']

    def parse(self, response):
        item = DdItem()
        item['title']=response.xpath('//a[@class="pic"]/@title').extract()
        item['link']=response.xpath('//a[@class="pic"]/@href').extract()
        item['comment'] = response.xpath('//a[@class="search_comment_num"]/text()').extract()
        item['image'] = response.xpath('//img/@data-original').extract()
        yield item
        for i in range(2,11):
            url = "http://category.dangdang.com/pg"+str(i)+"-cp01.54.06.19.00.00.html"
            yield Request(url,callback=self.parse)
