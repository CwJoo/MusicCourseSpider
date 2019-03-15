# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WkzjItem(scrapy.Item):
    title = scrapy.Field()
    course = scrapy.Field()
    grade = scrapy.Field()
    introduction = scrapy.Field()
    author = scrapy.Field()
    download = scrapy.Field()
    collection = scrapy.Field()
    browse = scrapy.Field()
    comment = scrapy.Field()
    time = scrapy.Field()

class CNweikeItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    play = scrapy.Field()
    time = scrapy.Field()
    vote = scrapy.Field()
    comment = scrapy.Field()
    collection = scrapy.Field()

class GXweikeItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    play = scrapy.Field()
    time = scrapy.Field()
    vote = scrapy.Field()
    comment = scrapy.Field()
    collection = scrapy.Field()

class QQweikeItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    buy = scrapy.Field()
    price = scrapy.Field()

class ChuankeItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    study = scrapy.Field()
    price = scrapy.Field()

class WangyiItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    study = scrapy.Field()
    price = scrapy.Field()