import requests
import json

class DoubanSpider:

    def __init__(self):
        self.url_list = ["https://m.douban.com/rexxar/api/v2/subject_collection/t"
                         "v_korean/items?start={}&count=18&loc_id=108288",
                         "https://m.douban.com/rexxar/api/v2/subject_collection/t"
                         "v_japanese/items?start={}&count=18&loc_id=108288",
                         "https://m.douban.com/rexxar/api/v2/subject_collection/t"
                         "v_animation/items?start={}&count=18&loc_id=108288"
                         ]
        self.headers = {"Referer":"https://m.douban.com/tv/korean",
                        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like"
                                      " Mac OS X) AppleWebKit/604.1.38 (KHTML, like "
                                      "Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

    def parsl_url(self, url):  # 请求数据
        html_str = requests.get(url, headers=self.headers)

        return html_str.content.decode()

    def getData(self, html_str):  # 获取数据
        html_str_to = json.loads(html_str)  # 转化为python数据类型
        # print(html_str_to)
        content_list = html_str_to["subject_collection_items"]
        return content_list

    def savaData(self, content_list):

        with open("douban.txt", "a", encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")  # 换行

    def run(self):
        for url_temp in self.url_list:
            # 1.获取url地址
            num = 0
            while True:
                url = url_temp.format(num)
                # 2.请求地址，获取响应
                html_str = self.parsl_url(url)
                # 3.提取数据
                content_list = self.getData(html_str)
                if len(content_list) < 18:
                    print(len(content_list))
                    break
                # 4.保存数据
                self.savaData(content_list)
                # 5.重新组织url地址
                num += 18


if __name__ == '__main__':
    douban = DoubanSpider()
    douban.run()
