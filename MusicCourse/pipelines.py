# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import xlwt,xlrd
from xlutils.copy import copy

class WkzjPipeline(object):

    row0 = ["标题","课程","年级","简介","作者","下载","收藏","浏览","评论","时间"]

    def __init__(self):
        rb = xlrd.open_workbook("MusicCourse.xls")
        self.fhandle = copy(rb)
        self.sheet = self.fhandle.add_sheet("wkzj", cell_overwrite_ok=True)
        self.row_num = 1
        self.init_row0()

    def init_row0(self):
        for i in range(len(WkzjPipeline.row0)):
            self.sheet.write(0, i, WkzjPipeline.row0[i])

    def process_item(self, item, spider):
        text = dict(item)
        self.sheet.write(self.row_num, 0 ,text["title"])
        self.sheet.write(self.row_num, 1 ,text["course"])
        self.sheet.write(self.row_num, 2 ,text["grade"])
        self.sheet.write(self.row_num, 3 ,text["introduction"])
        self.sheet.write(self.row_num, 4 ,text["author"])
        self.sheet.write(self.row_num, 5 ,text["download"])
        self.sheet.write(self.row_num, 6 ,text["collection"])
        self.sheet.write(self.row_num, 7 ,text["browse"])
        self.sheet.write(self.row_num, 8 ,text["comment"])
        self.sheet.write(self.row_num, 9 ,text["time"])
        self.row_num += 1
        
    def close_spider(self, spider):
        self.fhandle.save('MusicCourse.xls')

class CNweikePipeline(object):
    row0 = ["标题", "作者", "投票", "收藏", "播放", "评论", "时间"]

    def __init__(self):
        rb = xlrd.open_workbook("MusicCourse.xls")
        self.fhandle = copy(rb)
        self.sheet = self.fhandle.add_sheet("CNweike")
        self.row_num = 1
        self.init_row0()

    def init_row0(self):
        for i in range(len(CNweikePipeline.row0)):
            self.sheet.write(0, i, CNweikePipeline.row0[i])

    def process_item(self, item, spider):
        text = dict(item)
        self.sheet.write(self.row_num, 0 ,text["title"])
        self.sheet.write(self.row_num, 1 ,text["author"])
        self.sheet.write(self.row_num, 2 ,text["vote"])
        self.sheet.write(self.row_num, 3 ,text["collection"])
        self.sheet.write(self.row_num, 4 ,text["play"])
        self.sheet.write(self.row_num, 5 ,text["comment"])
        self.sheet.write(self.row_num, 6 ,text["time"])
        self.row_num += 1
        
    def close_spider(self, spider):
        self.fhandle.save('MusicCourse.xls')

class GXweikePipeline(object):
    row0 = ["标题", "作者", "投票", "收藏", "播放", "评论", "时间"]

    def __init__(self):
        rb = xlrd.open_workbook("MusicCourse.xls")
        self.fhandle = copy(rb)
        self.sheet = self.fhandle.add_sheet("CNweike", cell_overwrite_ok=True)
        self.row_num = 1
        self.init_row0()

    def init_row0(self):
        for i in range(len(CNweikePipeline.row0)):
            self.sheet.write(0, i, CNweikePipeline.row0[i])

    def process_item(self, item, spider):
        text = dict(item)
        self.sheet.write(self.row_num, 0 ,text["title"])
        self.sheet.write(self.row_num, 1 ,text["author"])
        self.sheet.write(self.row_num, 2 ,text["vote"])
        self.sheet.write(self.row_num, 3 ,text["collection"])
        self.sheet.write(self.row_num, 4 ,text["play"])
        self.sheet.write(self.row_num, 5 ,text["comment"])
        self.sheet.write(self.row_num, 6 ,text["time"])
        self.row_num += 1
        
    def close_spider(self, spider):
        self.fhandle.save('MusicCourse.xls')

class QQweikePipeline(object):
    row0 = ["标题", "作者", "购买|报名", "价格"]

    def __init__(self):
        rb = xlrd.open_workbook("MusicCourse.xls")
        self.fhandle = copy(rb)
        self.sheet = self.fhandle.add_sheet("QQweike", cell_overwrite_ok=True)
        self.row_num = 1
        self.init_row0()

    def init_row0(self):
        for i in range(len(QQweikePipeline.row0)):
            self.sheet.write(0, i, QQweikePipeline.row0[i])

    def process_item(self, item, spider):
        text = dict(item)
        self.sheet.write(self.row_num, 0 ,text["title"])
        self.sheet.write(self.row_num, 1 ,text["author"])
        self.sheet.write(self.row_num, 2 ,text["buy"])
        self.sheet.write(self.row_num, 3 ,text["price"])
        self.row_num += 1
        
    def close_spider(self, spider):
        self.fhandle.save('MusicCourse.xls')

class ChuankePipeline(object):
    row0 = ["标题", "作者", "学习", "价格"]

    def __init__(self):
        rb = xlrd.open_workbook("MusicCourse.xls")
        self.fhandle = copy(rb)
        self.sheet = self.fhandle.add_sheet("Chuanke", cell_overwrite_ok=True)
        self.row_num = 1
        self.init_row0()

    def init_row0(self):
        for i in range(len(ChuankePipeline.row0)):
            self.sheet.write(0, i, ChuankePipeline.row0[i])

    def process_item(self, item, spider):
        text = dict(item)
        self.sheet.write(self.row_num, 0 ,text["title"])
        self.sheet.write(self.row_num, 1 ,text["author"])
        self.sheet.write(self.row_num, 2 ,text["study"])
        self.sheet.write(self.row_num, 3 ,text["price"])
        self.row_num += 1
        
    def close_spider(self, spider):
        self.fhandle.save('MusicCourse.xls')

class WangyiPipeline(object):
    row0 = ["标题", "作者", "学习", "价格"]

    def __init__(self):
        rb = xlrd.open_workbook("MusicCourse.xls")
        self.fhandle = copy(rb)
        self.sheet = self.fhandle.add_sheet("Wangyi", cell_overwrite_ok=True)
        self.row_num = 1
        self.init_row0()

    def init_row0(self):
        for i in range(len(WangyiPipeline.row0)):
            self.sheet.write(0, i, WangyiPipeline.row0[i])

    def process_item(self, item, spider):
        text = dict(item)
        self.sheet.write(self.row_num, 0 ,text["title"])
        self.sheet.write(self.row_num, 1 ,text["author"])
        self.sheet.write(self.row_num, 2 ,text["study"])
        self.sheet.write(self.row_num, 3 ,text["price"])
        self.row_num += 1
        
    def close_spider(self, spider):
        self.fhandle.save('MusicCourse.xls')