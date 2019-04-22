# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Sun0769Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    number = scrapy.Field()  # 帖子编号
    title = scrapy.Field()  # 帖子标题
    url = scrapy.Field()  # 帖子链接
    content = scrapy.Field()  # 帖子内容
