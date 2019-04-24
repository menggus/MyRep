# -*- coding: utf-8 -*-
import scrapy
import urllib
from copy import deepcopy
import json


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com', 'p.3.cn']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        div_lsit = response.xpath("//div[@class='mc']/dl/dt")

        for dt in div_lsit:
            item = dict()
            item["first_cato"] = dt.xpath("./a/text()").extract_first()  # 获取图书一级分类
            # xpath 获取下一个兄弟节点  /current_point/following-sibling::b[index]
            dd_list = dt.xpath("./following-sibling::dd[1]/em") # 获取相邻节点的所有em子节点
            for em in dd_list:
                item["second_cato"] = em.xpath("./a/text()").extract_first()  # 获取二级分类
                item["url"] = em.xpath("./a/@href").extract_first()  # 获取二级分类的链接
                item["url"] = urllib.parse.urljoin(response.url, item["url"])  # 拼接url

                yield scrapy.Request(item["url"], callback=self.parse_books, meta={"item": deepcopy(item)})

    def parse_books(self, response):
        item = response.meta.get("item")

        div_lsit = response.xpath("//div[@id='plist']/ul/li")  # 获取图书列表

        for li in div_lsit:

            item["book_name"] = li.xpath(".//div[@class='p-name']/a/em/text()").extract_first().strip()  # 图书名,注意空格字符

            item["book_img"] =li.xpath(".//div[@class='p-img']/a/img/@src").extract_first()  # 图书图片地址
            if item["book_img"] is None:
                item["book_img"] ="https:" + li.xpath(".//div[@class='p-img']/a/img/@data-lazy-img").extract_first()
            else:
                item["book_img"] = "https:" + item["book_img"]

            item["book_url"] = "https:"+li.xpath(".//div[@class='p-img']/a/@href").extract_first()  # 图书的地址

            item["author"] = li.xpath(".//span[@class='p-bi-name']//a/@title").extract()  # 作者可能多人
            item["press"] = li.xpath(".//span[@class='p-bi-store']//a/@title").extract()  # 出版社

            item["press_date"] = li.xpath(".//span[@class='p-bi-date']/text()").extract_first().strip()

            # https://p.3.cn/prices/mgets?skuIds=J_12483068%2C  中 12483068为产品id
            # 价格不在当前响应中,需要重新请求地址
            books_id = li.xpath("./div/@data-sku").extract_first()
            if books_id is not None:
                price_url = "https://p.3.cn/prices/mgets?skuIds=J_{}".format(books_id)
                # print(item)
                # print(price_url, ">"*50)
                yield scrapy.Request(price_url, callback=self.parse_books_price, meta={"item": deepcopy(item)})

        # 翻页
        next_page = response.xpath("//div[@class='p-wrap']//a[@class='pn-next']/@href").extract_first()
        if next_page is not None:
            next_page = urllib.parse.urljoin(response.url, next_page)
            yield scrapy.Request(next_page, callback=self.parse_books, meta={"item": item})

    def parse_books_price(self, response):

        item = response.meta.get("item")

        item["book_price"] = json.loads(response.body.decode())[0]["op"]

        # print(item)

        yield item






















