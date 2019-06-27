import itchat
# 拼接
from PIL import Image
import os
import math
# 词云
import jieba
import pandas as pd
import re
from matplotlib import pyplot as plt
from wordcloud import WordCloud


class HeadImage:
    """
        生成好友拼接头像
        生产好友签名词云
    """

    def __init__(self):
        self.login = itchat.auto_login()
        self.name = None  # 你的微信名
        self.images_path = None  # 保存头像的文件夹路径
        self.count = None  # 好友数,图苏

    @staticmethod
    def get_friends_info():
        """
            获取好友信息
        :return: info
        """
        info = itchat.get_friends(update=True)

        return info

    def get_save_img(self, info):
        """
            获取好友头像,并保存
        :param info:
        :return:
        """
        if info is None:
            print("无任何好友信息.......")
            return
        # 创建存放头像的文件夹路径
        print(info)
        name = info[0].get("NickName")
        self.name = name
        images_path = "./{}_friends_image".format(name)
        if not os.path.exists(images_path):
            os.makedirs(images_path)
        self.images_path = images_path

        # 遍历好友信息,通过userName获取好友头像
        count = 0
        for i in info[1:]:
            username = i.get("UserName")
            nickname = i.get("NickName")
            image = itchat.get_head_img(userName=username)

            # 获取存储好友图像的路径
            image_path = images_path+"//"+"{}".format(nickname)+".jpg"
            try:
                with open(image_path, "wb") as f:
                    f.write(image)
            except Exception as e:
                print(e)
            count += 1
            print("正在保存第{}张图像".format(count))
        self.count = count
        print("好友图像保存成功..............")

    def image_splicing(self):
        """
            拼接头像
        :return:
        """
        # 头像文件名列表化
        image_path_list = os.listdir(self.images_path)

        # 计算拼接图,每行摆放多少个头像
        num = int(math.sqrt(self.count))

        # 创建拼图板
        splice_board = Image.new("RGB", (640, 640))
        single_size = int(640/num)  # 单个头像尺寸
        img_x, img_y = 0, 0  # 头像拼接坐标

        # 开始拼接
        for img in image_path_list[:num ** 2]:
            # 打开图像
            img_path = self.images_path + "//" + img
            try:
                img = Image.open(img_path)
            except IOError:
                print("文件不存在...........")
            else:
                # 对文件进行尺寸改变
                img = img.resize((single_size, single_size), Image.ANTIALIAS)
                # 放入拼接板
                splice_board.paste(img, (img_x*single_size, img_y*single_size))
                img_x += 1
                if img_x == num:
                    img_x = 0
                    img_y += 1
        splice_board.save("./{}_headimages.jpg".format(self.name))
        print("头像拼接保存成功............")

    def parse_friends(self, data):
        """
            解析好友数据并保存
        :param data: info
        :return: a dict
        """
        if data is None:
            return
        # 遍历好友信息,并保存
        for i in data[1:]:
            info = dict()
            info["Name"] = i.get("NickName")  # 昵称
            info["Rename"] = i.get("RemarkName")  # 备注昵称
            info["Sex"] = i.get("Sex")  # 性别
            info["Province"] = i.get("Province")  # 省份
            info["City"] = i.get("City")  # 城市AttrStatus
            info["AttrStatus"] = i.get("AttrStatus")  # 个性签名
            info["Signature"] = " ".join(i.get("Signature")) if "," in i.get("Signature") else i.get("Signature")  # 点赞数

            try:
                with open("{}_info.csv".format(self.name), "a+", encoding="utf-8") as f:
                    f.write("{},{},{},{},{},{},{}\n".format(info.get("Name"),
                                                            info.get("Rename"),
                                                            info.get("Sex"),
                                                            info.get("Province"),
                                                            info.get("City"),
                                                            info.get("Signature"),
                                                            info.get("AttrStatus")
                                                            ))
            except Exception as e:
                print(e)
        print("保存好友数据成功........")

    def data_clean(self, path):
        """
            处理保存好友数据,提取签名数据,并进行清洗
        :param path: 保存文件路径
        :return:
        """
        names = ["nickname", "name", "gender", "province", "city", "signature", "attrStatus"]
        data = pd.read_csv(path, header=None, names=names)
        # print(data.head())

        signature = data["signature"]  # 获取所有签名的数据
        signature = signature.dropna()  # 删除空签名

        word = ""
        for i in signature:
            # i = '随遇而安<span class="emoji emoji2764"></span>️'  # 测试替换成功
            if "<" or ">" in i:
                i = re.sub(r"<.*?>", "", i)
            i = " ".join(jieba.analyse.extract_tags(i, 5))  # 基于TF-IDF 算法的关键词抽取
            word += i

        return word

    def creat_wordcloud(self, word):
        """
            创建词云图
        :param word: 需要生产词云的文本
        :return: None
        """
        # 读取图片背景
        background = plt.imread("1.png")

        # 设置词云样式
        word_style = WordCloud(font_path="/usr/share/fonts/truetype/arphic/ukai.ttc",  # 设置字体
                               background_color="lightpink",  # 设置背景颜色
                               max_words=200,  # 设置显示词云的数量
                               mask=background)  # 背景图

        # 将词汇导入
        word_style.generate(word)

        # 存储词云图
        word_style.to_file("2.png")


    @staticmethod
    def login_out():
        itchat.logout()


if __name__ == '__main__':
    my = HeadImage()

    # 获取好友信息
    info = my.get_friends_info()

    # 获取好友图像,并存储
    my.get_save_img(info)

    # 关闭itchat
    my.login_out()

    # 拼接头像
    my.image_splicing()