# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TtSpider(CrawlSpider):
    name = 'tt'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (
        # 匹配详情页地址
        # href="position_detail.php?id=49677&keywords=&tid=0&lid=0"
        # href="position_detail.php?id=49678&keywords=&tid=0&lid=0"
        Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+&keywords=&tid=0&lid=0'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+#a'), follow=True),
        # 匹配翻页地址
        # href="position.php?&start=10#a"
    )

    def parse_item(self, response):

        item = dict()

        item['title'] = response.xpath(
            "//table[@class='tablelist textl']/tr[@class='h']/td/text()").extract_first()
        item['area'] = response.xpath(
            "//table[@class='tablelist textl']/tr[@class='c bottomline']/td[1]/text()").extract_first()
        item['catogroy'] = response.xpath(
            "//table[@class='tablelist textl']/tr[@class='c bottomline']/td[2]/text()").extract_first()
        item['number'] = response.xpath(
            "//table[@class='tablelist textl']/tr[@class='c bottomline']/td[3]/text()").extract_first()

        print(item)
        return item
