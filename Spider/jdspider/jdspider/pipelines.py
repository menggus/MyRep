# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time

class JdspiderPipeline(object):
    def process_item(self, item, spider):

        item["parse_date"] = time.ctime()

        return item
