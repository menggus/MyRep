# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
import urllib
import re
import logging

class AmazonSpider(RedisCrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    # start_urls = ['https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=sd_allcat_books_l1?ie=UTF8&node=658390051']
    redis_key = 'amazon'

    rules = (
        # 页面较复杂,采用xpath
        Rule(
            LinkExtractor(restrict_xpaths=["//ul[@class='a-unordered-list a-nostyle a-vertical s-ref-indent-one']//li"])
        ),
        Rule(
            LinkExtractor(restrict_xpaths=["//ul[@class='a-unordered-list a-nostyle a-vertical s-ref-indent-two']//li"]),
            follow=True
        ),
        Rule(
            LinkExtractor(restrict_xpaths=["//h2"]),
            callback="parse_books"
        ),
        Rule(LinkExtractor(
            restrict_xpaths=["//div[@id='bottomBar']/div/span[@class='pagnLink']/a"]),
            follow=True
        ),
    )

    def parse_books(self, response):

        item = dict()
        # 书名
        item["book_name"] = response.xpath("//h1[@id='title']/span[1]/text()").extract_first()
        if item["book_name"] is not None:
            item["book_name"] = item["book_name"].strip()

        # 书地址
        item["book_url"] = response.url

        # 作者
        item["author"] = response.xpath("//div[@id='bylineInfo']/span//text()").extract()
        item["author"] = [i.strip() for i in item["author"] if len(i.strip()) > 0]
        if item["author"] is not None:
            item["author"] = " ".join(item["author"])
            item["author"] = item["author"].split("&")[0]

        # 出版社 和出版日期
        item["press"] = response.xpath("//b[text()='出版社:']/../text()").extract_first()
        if item["press"]:
            item["press"] = item["press"].strip()

        # 价格
        item["price"] = response.xpath("//span[@class='a-size-medium a-color-price inlineBlock-display offer-price "
                                       "a-text-normal price3P']/text()").extract_first()
        # 有些只有电子书价格
        if item["price"] is None:
            item["price"] = response.xpath("//tr[@class='kindle-price']/td[2]/text()").extract_first()
            if item["price"] is not None:
                item["price"] = item["price"].strip()

        # 图片base 64 编码
        # item["book_img"] = response.xpath("//img[@id='imgBlkFront']/@src").extract_first()
        # if item["book_img"] is not None:
        #     item["book_img"] = re.findall(r"&quot;(.*?)&quot;", item["book_img"])[0]

        cato = response.xpath("//div[@id='wayfinding-breadcrumbs_feature_div']/ul/li").extract_first()
        item["len"] = len(cato)


        logging.warning(item)

















