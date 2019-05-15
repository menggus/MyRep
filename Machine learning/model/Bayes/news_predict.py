# coding: utf-8

from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report


def bayes():
    # #### 获取数据
    #     new.DESCR:数据描述
    #     news.data:数据
    #     news.filesname: 文件名
    #     news.target: 目标值
    #     news.target_names: 目标分类

    # 获取数据

    news = fetch_20newsgroups(subset="all")

    # 数据集分割

    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25)  # 分割


    # #### 特征工程
    #     CountVectorizer：统计词出现的数量，来作为分类的依据；（存在问题：一个词在每个文档中都出现，且次数多，但不能作为分类依
    #                      据，与分类毫无关系），例：今天、其他、所以等。
    #     TfidfVectorizer：在统计词频时，加入了一个权重，即词的一个是否能作为分类依据的重要性，也就解决上述存在问题
    #
    #     如一个文档，其中一次在每个文档中都出现，就不会作为分类依据
    #     因为：tf：在当前文本中高，但是idf为1，但一次在该文本中只有1/10概率，但是在idf上来看，只出现在一个文本中，则idf=10（总文本数）
    #     所以同样的词，后者的重要性可想而知，可作为分类依据。
    #
    #     tf: 当前文本中词出现的频率 , 仅考虑当前文本是重要的
    #     idf：总文本数/出现该特征的文本数
    #     Tfidf = tf*idf

    # 特征值提取，以重要性方法

    tf = TfidfVectorizer()
    x_train_trans = tf.fit_transform(x_train)
    x_test_trans = tf.transform(x_test)

    # #### 朴素贝叶斯进行模型训练

    bayes = MultinomialNB(alpha=1.0)  # 实例化 alpha 拉普拉斯平滑系数 1.0
    bayes.fit(x_train_trans, y_train)  # 传入数据训练数据
    result = bayes.predict(x_test_trans)  # 预测

    # 结果

    print(result)  # 预测结果
    print(bayes.score(x_test_trans, y_test))  # 输入测试集，得出准确率

    # #### 查看精确率，召回率
    #     classification_report(真实值， 预测值， 目标分类名称)

    print(classification_report(y_test, result, target_names=news.target_names))



