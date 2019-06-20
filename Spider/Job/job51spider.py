import requests
from lxml import etree
import re

class JobSpider:

    def __init__(self, url):
        self.start_url = url
        self.headers = {
            "Host": "search.51job.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                          "75.0.3770.100 Safari/537.36"
        }

    def parse_url(self, url):
        response = requests.get(url, headers=self.headers, timeout=10)
        #
        s = requests.session()
        s.keep_alive = False

        return response.content.decode(encoding="gbk")

    def extract(self, data):
        html = etree.HTML(data)

        posi = dict()

        posi["position"] = html.xpath("//div[@class='tHeader tHjob']//h1/@title")[0] if len(
            html.xpath("//div[@class='tHeader tHjob']//h1/@title")) > 0 else None

        posi["salary"] = html.xpath("//div[@class='tHeader tHjob']//strong/text()")[0] if len(
            html.xpath("//div[@class='tHeader tHjob']//strong/text()")) > 0 else None

        posi["company"] = html.xpath("//div[@class='tHeader tHjob']//p[@class='cname']/a[1]/@title")[0] if len(
            html.xpath("//div[@class='tHeader tHjob']//p[@class='cname']/a[1]/@title")) > 0 else None

        info = html.xpath("//div[@class='tHeader tHjob']//p[@class='msg ltype']/@title")[0] if len(
            html.xpath("//div[@class='tHeader tHjob']//p[@class='msg ltype']/@title")) > 0 else None

        # 去掉句子中的\xa0\xa0，连续空格
        info = "".join(info.split())

        info = [i.strip() for i in info.split("|")]
        print(info)
        posi["area"] = info[0] if len(info) > 0 else None
        posi["experience"] = info[1] if len(info) > 1 else None
        posi["education"] = info[2] if len(info) > 2 else None

        # 采用xpath中的string()获取所有子节点的文本
        re_con = html.xpath("//div[@class='bmsg job_msg inbox']") if len(
            html.xpath("//div[@class='bmsg job_msg inbox']")) > 0 else None
        re_con = re_con[0].xpath("string(.)")
        posi["require"] = "".join(re_con.split())

        return posi

    def save(self, unit):
        print(unit)
        with open("job.csv", "a+", encoding="utf-8") as f:
            f.write("{},{},{},{},{},{},{}\n".format(
                unit.get("position"),
                unit.get("salary"),
                unit.get("company"),
                unit.get("area"),
                unit.get("experience"),
                unit.get("education"),
                unit.get("require")
            ))
        print("*"*20+"OK"+"*"*20)

    def run(self):
        # 循环爬取
        page = 1
        while True:
            # 获取start_url请求数据
            response = self.parse_url(self.start_url)
            # 解析内容
            con_html = etree.HTML(response)
            # 当前页的所有职位的url列表
            url_list = con_html.xpath("//p[@class='t1 ']/span/a[@target='_blank']/@href")
            print(url_list)
            print("开始爬取第{}页".format(page))
            # 遍历
            for i in url_list:
                # 2.parse_url获取数据
                res = self.parse_url(i)
                # 3.数据提取
                unit = self.extract(res)
                # 4.数据的保存
                self.save(unit)

            next_url = con_html.xpath("//div[@class='dw_page']//ul/li/a[text()='下一页']/@href")[0] if len(
                con_html.xpath("//div[@class='dw_page']//ul/li/a[text()='下一页']/@href")) > 0 else None
            if next_url is None:
                break
            else:
                self.start_url = next_url
            page += 1


if __name__ == '__main__':
    start_url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html"
    spider = JobSpider(start_url)
    spider.run()
