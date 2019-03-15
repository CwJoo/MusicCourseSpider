# -*- coding: utf-8 -*-
import scrapy
from MusicCourse.items import CNweikeItem
import json

class CnweikeSpider(scrapy.Spider):
    name = 'cnweike'
    allowed_domains = ['cnweike.cn']
    url = 'http://dasai.cnweike.cn/index.php?r=matchV4/search/GetJson&pageSize=10&type=weike&order=quality&keyword=&subject=7&pointOne=0&pointTwo=0&pointThree=0&typeID=51&page='

    custom_settings = {
        "ITEM_PIPELINES": {
            'MusicCourse.pipelines.CNweikePipeline': 300,
        }
    }

    offset = 1
    start_urls = [url + str(offset)]

    def parse(self, response):
        page_dict = json.loads(response.body)
        for course_item in page_dict["data"]:
            item = CNweikeItem()
            item['title'] = course_item['fdName']
            item['author'] = course_item['fdUser']
            item['play'] = course_item['fdPlay']
            item['time'] = course_item['fdCreate']
            item['vote'] = course_item['voteNum']
            item['collection'] = course_item['collectnum']
            item['comment'] = course_item['commnets']
            yield item

        if self.offset < 45:
            self.offset += 1

        # 每次处理完一页的数据之后，重新发送下一页页面请求
        # self.offset自增10，同时拼接为新的url，并调用回调函数self.parse处理Response
        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)

