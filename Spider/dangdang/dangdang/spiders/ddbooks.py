# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
from scrapy_redis.spiders import RedisSpider
import urllib


class DdbooksSpider(RedisSpider):
    name = 'ddbooks'
    allowed_domains = ['dangdang.com']
    # start_urls = ['http://book.dangdang.com/']
    redis_key = "dangdang:books"

    def parse(self, response):
        # print(response.body.decode())
        div_list = response.xpath("//div[@class='level_one ']")[2:13]

        for div in div_list:
            item = dict()
            # 当当一级分类名,结构多样,这里直接取全部,之后再对数据进行处理
            item["first_cato"] = div.xpath("./dl/dt//text()").extract() # 一级分类名
            item["first_cato"] = " ".join([i.strip() for i in item["first_cato"] if i.strip() is not ""])
            dl_list = div.xpath("./div//dl[@class='inner_dl']")  # 二级分类列表

            for dl in dl_list:
                item["second_cato"] = dl.xpath("./dt/a/text()").extract()  # 二级分类名
                item["second_cato"] = " ".join([i.strip() for i in item["second_cato"] if i.strip() is not ""])
                a_list = dl.xpath("./dd/a")[0:-1]  # 二级分类列表

                for a in a_list:
                    item["third_cato"] = a.xpath("./text()").extract_first().strip()  # 三级分类名
                    item["cato_url"] = a.xpath("./@href").extract_first()  # 三级分类url地址
                    if item["cato_url"] is not None:
                        yield scrapy.Request(item["cato_url"], callback=self.parse_books, meta={"item": deepcopy(item)})

    def parse_books(self, response):

        item = response.meta.get("item")

        li_list = response.xpath("//ul[@class='bigimg']/li")  # 图书列表

        """抓取当当图书又有图书的名字、封面图片地址、图书url地址、作者、出版社、
        出版时间、价格、图书所属大分类、图书所属小的分类、分类的url地址
        """

        # 结果1

        for li in li_list:
            item["book_name"] = li.xpath("./a/@title").extract_first().strip()
            item["book_img"] = li.xpath("./a/img/@src").extract_first()
            if item["book_img"] == "images/model/guan/url_none.png":
                item["book_img"] = li.xpath("./a/img/@data-original").extract_first()
            item["book_url"] = li.xpath("./a/@href").extract_first()
            item["author"] = li.xpath("./p[@class='search_book_author']/span[1]/a/text()").extract()  # 多个作者
            if item["author"] is not None:
                item["author"] = " ".join(item["author"])
            item["press"] = li.xpath("./p[@class='search_book_author']/span[3]/a/@title").extract_first()
            item["press_date"] = li.xpath("./p[@class='search_book_author']/span[2]/text()").extract_first()
            if item["press_date"] is not None:
                item["press_date"] = item["press_date"].split(r"/")[1]

            item["price"] = li.xpath(".//span[@class='search_now_price']/text()").extract_first()

            yield deepcopy(item)
            # yield item


        # 翻页
        next_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if next_page is not None:
            next_page = urllib.parse.urljoin(response.url, next_page)
            yield scrapy.Request(next_page, callback=self.parse_books, meta={"item": deepcopy(item)})

