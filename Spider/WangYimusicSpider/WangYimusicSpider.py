import requests
from selenium import webdriver
import time
import json

class WangYimusicSpider:

    def __init__(self):
        self.language = ["华语", "欧美", "日语", "韩语", "粤语", "小语种"]
        self.temp_url = "https://music.163.com/#/discover/playlist/?cat={}"
        self.driver = webdriver.Chrome()

    def get_url(self):
        """ 获取url
        :return:    url列表
        """
        return [self.temp_url.format(i) for i in self.language]

    def driver_url(self, url):
        """ 发送请求

        :param url: url地址
        :return:    响应内容
        """
        self.driver.get(url)
        song_list = []  # 单语种下的歌单 [{"title":  , "href":}, ...]

        num = 0

        while True:
            hand = self.driver.window_handles
            print(hand)
            self.driver.switch_to.window(hand[0])
            self.driver.switch_to.frame("g_iframe")  # 云音乐内嵌iframe
            elements_list = self.driver.find_elements_by_xpath("//ul[@id='m-pl-container']/li/div/a")

            for element in elements_list:
                song_dict = dict()
                song_dict["title"] = element.get_attribute("title")
                song_dict["href"] = element.get_attribute("href")
                song_list.append(song_dict)
                print(song_dict)
            # print(song_list)
            next_page = self.driver.find_element_by_xpath("//a[text()='下一页']")
            if num > 1:
                break
            num += 1
            if "js-disabled" in next_page.get_attribute("class"):
                # 最后一页
                break
            else:
                # 这里如果使用next_page.click()会作用到别的元素上，执行脚本可以跳转
                self.driver.execute_script("arguments[0].click()", next_page)
                print("-"*100)
                time.sleep(5)

        return song_list

    def extraction_detail_data(self, item):
        """ 提取歌单响应数据

        :param item:    响应
        :return:    返回数据
        """
        # info = {
        #     "language": "语言",
        #     "songlist": [
        #         {"歌单信息"},
        #         {"歌单信息"}
        #     ]
        # }
        info = dict()
        info["language"] = item["language"]
        info["song_list"] = []
        for item in item["url_list"]:
            detail_song_dict = dict()
            self.driver = webdriver.Chrome()
            self.driver.get(item["href"])
            self.driver.switch_to.frame("g_iframe")
            detail_song_dict["username"] = self.driver.find_element_by_class_name("s-fc7").text
            # detail_song_dict["creat_time"] = self.driver.find_element_by_class_name("time s-fc4").text
            detail_song_dict["fav"] = \
                self.driver.find_element_by_xpath("//a[@data-res-action='fav']").get_attribute("data-count")
            detail_song_dict["share"] = \
                self.driver.find_element_by_xpath("//a[@data-res-action='share']").get_attribute("data-count")
            detail_song_dict["comment"] = \
                self.driver.find_element_by_xpath("//span[@id='cnt_comment_count']").text
            detail_song_dict["playlist"] = \
                self.driver.find_element_by_xpath("//span[@id='playlist-track-count']").text
            detail_song_dict["playcount"] = \
                self.driver.find_element_by_xpath("//strong[@id='play-count']").text

            # 歌曲信息
            detail_song_dict["music_info"] = []
            music_list = self.driver.find_elements_by_xpath("//tbody/tr")
            for music in music_list:
                music_info = dict()
                music_info["name"] = music.find_element_by_xpath("./td//span[@class='txt']/a/b").get_attribute("title")
                music_info["singer"] = music.find_element_by_xpath("./td/div[@class='text']").get_attribute("title")
                music_info["link"] = music.find_element_by_xpath("./td//span[@class='txt']/a").get_attribute("href")
                music_info["time"] = music.find_element_by_xpath("./td/span[@class='u-dur ']").text
                detail_song_dict["music_info"].append(music_info)
            print(detail_song_dict)
            info["song_list"].append(detail_song_dict)
            self.driver.quit()
            break
        print(info)
        return info

    def sava_data(self, resu):
        """
            保存数据结果为文件
        :param resu:
        :return:
        """
        with open("song.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(resu, ensure_ascii=False, indent=4))
            f.write("\n")

    def run(self):
        # 1.url
        url_list = self.get_url()
        # 2.请求，获取响应,歌单的标题和所有歌单地址
        div_language_music_list = []
        for language, url in zip(self.language, url_list):
            song_list = dict()
            song_list["language"] = language
            song_list["url_list"] = self.driver_url(url)
            div_language_music_list.append(song_list)
            print(song_list)
            break

        # 3.提取详情页数据
        for item in div_language_music_list:
            content = self.extraction_detail_data(item)
            # 4.保存数据
            self.sava_data(content)

        # 5.
        self.driver.quit()


if __name__ == '__main__':
    wangyi = WangYimusicSpider()
    wangyi.run()
