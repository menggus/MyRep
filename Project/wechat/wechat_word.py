import pandas as pd
import re
import jieba.analyse
from wordcloud import WordCloud
from matplotlib import pyplot as plt

"""
    创建词云
"""

def data_clean(path):
    """
        获取数据,进行数据处理
    :param path: 数据路径
    :return: 返回清洗后的数据-- 好友签名
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

def creat_wordcloud(word):
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


if __name__ == '__main__':
    path = "friends.csv"
    # 1.数据处理
    word = data_clean(path)
    # 2.词云生产
    creat_wordcloud(word)
