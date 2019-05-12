from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split


def news_categroy_predict():
    """
        朴素贝叶斯进行文本分类
    :return:
    """
    # 获取新闻数据
    news = fetch_20newsgroups(subset="all")

    # 对数据集进行分割
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25)

    #
    print(x_train)
