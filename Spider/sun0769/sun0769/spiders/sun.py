# -*- coding: utf-8 -*-
import scrapy
from sun0769.items import Sun0769Item


class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):
        data_list = response.xpath("//div[@class='greyframe']//table[2]//tr/td//tr")

        for data in data_list:
            item = Sun0769Item()
            item["number"] = data.xpath("./td[1]/text()").extract_first()
            item["title"] = data.xpath("./td[2]/a[@class='news14']/text()").extract_first()
            item["url"] = data.xpath("./td[2]/a[@class='news14']/@href").extract_first()

            yield scrapy.Request(item["url"], callback=self.parse_detail, meta={"item": item})

        next_url = response.xpath("//div[@class='pagination']/a[text()='>']/@href").extract_first()

        print(next_url)
        if next_url is not None:
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, response):
        item = response.meta["item"]
        item["content"] = response.xpath("//div[@class='wzy1']//td[@class='txt16_3']/text()").extract_first()

        yield item