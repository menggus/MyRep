import requests
from selenium import webdriver
import time
import json
from queue import Queue
from threading import Thread


class WangYimusicSpider:

    def __init__(self):
        self.language = ["华语", "欧美", "日语", "韩语", "粤语", "小语种"]
        self.temp_url = "https://music.163.com/#/discover/playlist/?cat={}"
        self.driver_url_queue = Queue()
        self.extraction_detail_data_queue = Queue()
        self.sava_data_queue = Queue()

    def get_url(self):
        """ 获取url
        :return:    url列表
        """
        for lan in self.language:
            song_list = dict()
            url = self.temp_url.format(lan)
            song_list["language"] = lan
            song_list["url_list"] = url
            self.driver_url_queue.put(song_list)

    def driver_url(self):
        """ 发送请求

        :return:    响应内容
        """
        while True:
            driver = webdriver.Chrome()
            song_list_url = self.driver_url_queue.get()
            print(song_list_url["url_list"])
            driver.get(song_list_url["url_list"])
            song_list = []  # 单语种下的歌单 [{"title":  , "href":}, ...]
            num = 0  # 控制爬取页面数
            while True:
                hand = driver.window_handles
                driver.switch_to.window(hand[0])
                driver.switch_to.frame("g_iframe")  # 云音乐内嵌iframe
                elements_list = driver.find_elements_by_xpath("//ul[@id='m-pl-container']/li/div/a")

                for element in elements_list:
                    song_dict = dict()
                    song_dict["title"] = element.get_attribute("title")
                    song_dict["href"] = element.get_attribute("href")
                    song_list.append(song_dict)

                print(song_list)
                next_page = driver.find_element_by_xpath("//a[text()='下一页']")

                """
                网易云音乐，歌单最后一页判断条件
                if "js-disabled" in next_page.get_attribute("class"):
                     # 最后一页
                """
                if num == 1:

                    break
                else:
                    # 这里如果使用next_page.click()会作用到别的元素上，执行脚本可以跳转
                    driver.execute_script("arguments[0].click()", next_page)
                    num += 1
                    time.sleep(5)

            result = dict()
            result["language"] = song_list_url["language"]
            result["url_list"] = song_list

            self.extraction_detail_data_queue.put(result)
            self.driver_url_queue.task_done()
            driver.quit()  # 关闭浏览器

    def extraction_detail_data(self):
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
        while True:
            item = self.extraction_detail_data_queue.get()
            info = dict()
            info["language"] = item["language"]
            info["song_list"] = []
            for item in item["url_list"]:
                detail_song_dict = dict()
                driver = webdriver.Chrome()
                driver.get(item["href"])
                print("")
                print("请求歌单详情地址：{}".format(item["href"]))
                driver.switch_to.frame("g_iframe")
                detail_song_dict["username"] = driver.find_element_by_class_name("s-fc7").text
                # detail_song_dict["creat_time"] = self.driver.find_element_by_class_name("time s-fc4").text
                detail_song_dict["fav"] = \
                    driver.find_element_by_xpath("//a[@data-res-action='fav']").get_attribute("data-count")
                detail_song_dict["share"] = \
                    driver.find_element_by_xpath("//a[@data-res-action='share']").get_attribute("data-count")
                detail_song_dict["comment"] = \
                    driver.find_element_by_xpath("//span[@id='cnt_comment_count']").text
                detail_song_dict["playlist"] = \
                    driver.find_element_by_xpath("//span[@id='playlist-track-count']").text
                detail_song_dict["playcount"] = \
                    driver.find_element_by_xpath("//strong[@id='play-count']").text

                # 歌曲信息
                detail_song_dict["music_info"] = []
                music_list = driver.find_elements_by_xpath("//tbody/tr")
                for music in music_list:
                    music_info = dict()
                    music_info["name"] = music.find_element_by_xpath("./td//span[@class='txt']/a/b").get_attribute("title")
                    music_info["singer"] = music.find_element_by_xpath("./td/div[@class='text']").get_attribute("title")
                    music_info["link"] = music.find_element_by_xpath("./td//span[@class='txt']/a").get_attribute("href")
                    music_info["time"] = music.find_element_by_xpath("./td/span[@class='u-dur ']").text
                    detail_song_dict["music_info"].append(music_info)
                print(detail_song_dict)
                info["song_list"].append(detail_song_dict)
                driver.quit()
                print("获取单个歌单内容完毕")
            self.sava_data_queue.put(info)
            self.extraction_detail_data_queue.task_done()

    def sava_data(self):
        """
            保存数据结果为文件
        :param resu:
        :return:
        """
        while True:
            resu = self.sava_data_queue.get()
            with open("song.json", "a", encoding="utf-8") as f:
                f.write(json.dumps(resu, ensure_ascii=False, indent=4))
                f.write("\n")
            print("保存成功")
            self.sava_data_queue.task_done()

    def run(self):
        # 1.url
        self.get_url()

        task_list = []
        # 2.请求，获取响应,歌单的标题和所有歌单地址
        for i in range(3):
            url_list = Thread(target=self.driver_url)
            task_list.append(url_list)
        # 3.提取详情页数据
        for i in range(5):
            song_list_task = Thread(target=self.extraction_detail_data)
            task_list.append(song_list_task)
        # 5.保存数据
        for i in range(2):
            sava_data_task = Thread(target=self.sava_data)
            task_list.append(sava_data_task)

        # 6.开启线程
        for i in task_list:
            i.setDaemon(True)  # 设置子线程为守护线程，当主线程结束，子线程结束
            i.start()

        # 7.阻塞主线程，等待子线程结束
        for q in [self.driver_url_queue, self.extraction_detail_data_queue, self.sava_data_queue]:
            q.join()


if __name__ == '__main__':
    wangyi = WangYimusicSpider()
    wangyi.run()
