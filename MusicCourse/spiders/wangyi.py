# -*- coding: utf-8 -*-
import scrapy
from MusicCourse.items import WangyiItem
import json

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    allowed_domains = ['163.com']

    
    custom_settings = {
        "ITEM_PIPELINES": {
            'MusicCourse.pipelines.WangyiPipeline': 300,
        },
        "DEFAULT_REQUEST_HEADERS":{
            'Host': "study.163.com",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0",
            'Accept': "application/json",
            'Referer': "https://study.163.com/category/480000003132052",
        }
    }

    def start_requests(self):

        payload = {
            'pageIndex': '1',
            'pageSize': '50',
            'relativeOffset': '0',
            'frontCategoryId':'480000003132052',
            'searchTimeType': '-1',
            'orderType': '10',
            'priceType': '-1',
            'activityId': '0',
            'keyword':''
        }

        url = 'https://study.163.com/p/search/studycourse.json'
        yield scrapy.FormRequest(url, formdata=payload, callback=self.parse_list)

    def parse_list(self, response):
        page_dict = json.loads(response.body)
        course_dict = page_dict["result"]["list"]
        item = WangyiItem()
        for course_detail in course_dict:
            item["title"] =  course_detail["productName"]
            item["author"] = course_detail["provider"]
            item["study"] = course_detail["learnerCount"]
            item["price"] = course_detail["originalPrice"]
            yield item
        
        
