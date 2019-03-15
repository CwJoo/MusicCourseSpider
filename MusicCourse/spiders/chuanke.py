# -*- coding: utf-8 -*-
import scrapy
from MusicCourse.items import ChuankeItem

class ChuankeSpider(scrapy.Spider):
    name = 'chuanke'
    allowed_domains = ['baidu.com']
    url = 'https://chuanke.baidu.com/course/_%E9%9F%B3%E4%B9%90_____.html?page='

    custom_settings = {
        "ITEM_PIPELINES": {
            'MusicCourse.pipelines.ChuankePipeline': 300,
        }
    }

    offset = 1
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//div[@class='item-panel']"):
            # 初始化模型对象
            item = ChuankeItem()
            # 标题
            item['title'] = each.xpath(".//div[@class='item-title']//a//text()").extract()
            # 作者
            item['author'] = each.xpath(".//div[@class='school-name']//a//text()").extract()
            # 购买|报名
            item['study'] = each.xpath(".//div[@class='number']//em//text()").extract()
            # 价格
            item['price'] = each.xpath(".//div[@class='price']//span//text()").extract()
            yield item

        if self.offset < 18:
            self.offset += 1

        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
