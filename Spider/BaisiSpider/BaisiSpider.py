import requests
import re


class BaisiSpider:

    def __init__(self):
        self.url = "http://m.budejie.com/{}"
        self.headers = {
            "Cookie": "_ga=GA1.2.2074955451.1554972506; _gid=GA1.2.1880121582.1554972506;"
                      " Hm_lvt_7c9f93d0379a9a7eb9fb60319911385f=1554972506,1554972603; _"
                      "gat=1; Hm_lpvt_7c9f93d0379a9a7eb9fb60319911385f=1554972798",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) "
                          "AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/"
                          "15A372 Safari/604.1",
        }

    def parsl_url(self, url):

        html_st = requests.get(url, headers=self.headers)

        return html_st.content.decode()

    def getData(self, content_data):
        # print(content_data)

        cont_list = re.findall(r'<p>(.*?)</p>', content_data, re.S)
        print(cont_list)

        return cont_list

    def saveData(self, cont_list):

        with open("baisi.txt", "a", encoding="utf-8") as f:
            for cont in cont_list:
                f.write(cont)
                f.write("\n")

    def run(self):
        num = 0
        while True:
            # 1.获取url地址
            url = self.url.format(num)
            # 2.爬取数据
            content_data = self.parsl_url(url)
            # 3.提取数据
            cont_list = self.getData(content_data)
            # 4.保存数据
            self.saveData(cont_list)
            # 5.重置url
            num += 1
            if num>50:
                break


if __name__ == '__main__':
    baisi = BaisiSpider()
    baisi.run()