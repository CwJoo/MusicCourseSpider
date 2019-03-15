# -*- coding: utf-8 -*-
import scrapy
from MusicCourse.items import QQweikeItem

class KeqqSpider(scrapy.Spider):
    name = 'keqq'
    allowed_domains = ['qq.com']
    url = 'https://ke.qq.com/course/list/%E9%9F%B3%E4%B9%90?page='

    custom_settings = {
        "ITEM_PIPELINES": {
            'MusicCourse.pipelines.QQweikePipeline': 300,
        }
    }

    offset = 1
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//div[@class='main-left']//li[@class='course-card-item']"):
            # 初始化模型对象
            item = QQweikeItem()
            # 标题
            item['title'] = each.xpath(".//h4[@class='item-tt']//a//text()").extract()[0]
            # 作者
            item['author'] = each.xpath(".//span[@class='item-source']//a[@class='item-source-link']//text()").extract()[0]
            # 购买|报名
            item['buy'] = each.xpath(".//span[@class='line-cell item-user']//text()").extract()[0].split()
            # 价格
            item['price'] = each.xpath(".//div[@class='item-line item-line--bottom']//span//text()").extract()[0]
            yield item

        if self.offset < 36:
            self.offset += 1

        yield scrapy.Request(self.url+str(self.offset), callback=self.parse)
