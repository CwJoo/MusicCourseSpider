# -*- coding: utf-8 -*-
import scrapy
from MusicCourse.items import WkzjItem

class WkzjSpider(scrapy.Spider):
    name = 'wkzj'
    allowed_domains = ['wkzj.com']
    url = 'https://www.wkzj.com/shared/resources/index?gradedesc=all&subjectdesc=音乐&bookletdesc=all&keyword=&page='

    custom_settings = {
        "ITEM_PIPELINES": {
            'MusicCourse.pipelines.WkzjPipeline': 300,
        }
    }

    offset = 1
    start_urls = [url + str(offset)]

    def parse(self, response):
        for each in response.xpath("//div[@class='resource-list']"):
            # 初始化模型对象
            item = WkzjItem()
            # 标题
            item['title'] = each.xpath(".//h3/text()").extract()[0].strip()
            # 课程
            item['course'] = each.xpath(".//div[@class='kemu_style']/text()").extract()[1].split("\r\n")[0].strip()
            # 年级
            item['grade'] = each.xpath(".//div[@class='kemu_style']/text()").extract()[1].split("\r\n")[1].strip()
            # 介绍
            item['introduction'] = each.xpath(".//div[@class='kemu_style info-elip']/text()").extract()[0].strip()
            # 作者
            item['author'] = each.xpath(".//div[@class='kemu_style']/a/text()").extract()[0].strip()
            # 下载
            item['download'] = each.xpath(".//div[@class='kemu_style']/text()").extract()[4].split()[0]
            # 收藏
            item['collection'] = each.xpath(".//div[@class='kemu_style']/text()").extract()[4].split()[1]
            # 浏览
            item['browse'] = each.xpath(".//div[@class='kemu_style']/text()").extract()[4].split()[2]
            # 评论
            item['comment'] = each.xpath(".//div[@class='kemu_style']/text()").extract()[4].split()[3]
            # 时间
            item['time'] = each.xpath(".//span/text()").extract()[0].strip()
            yield item

        if self.offset < 18:
            self.offset += 1

        yield scrapy.Request(self.url + str(self.offset), callback = self.parse)
