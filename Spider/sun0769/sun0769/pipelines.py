# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

client = MongoClient()
collection = client["sundb"]["sun"]


class Sun0769Pipeline(object):
    def process_item(self, item, spider):

        item["content"] = item["content"].strip()
        collection.insert_one(dict(item))

        return item

    def rm_space(self, data):
        """
            去除空白字符
        :param data: 传入的参数
        :return:
        """
        pass

