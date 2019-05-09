from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd
from matplotlib import pyplot as plt


def iris_predicting():
    """
        鸢尾花预测
    :return:
    """
    # 获取数据
    data = load_iris()

    feature_data = data.data
    target_data = data.target

    # 划分数据集 ，特征训练，特征测试，目标训练，目标测试
    feature_train, feature_test, target_train, target_test = train_test_split(feature_data, target_data, test_size=0.25)

    # 特征工程，标准化
    std = StandardScaler()
    feature_train = std.fit_transform(feature_train)
    feature_test = std.transform(feature_test)

    # knn, K邻近
    knn = KNeighborsClassifier()
    knn.fit(feature_train, target_train)  # fit 输入训练数据
    predict = knn.predict(feature_test)

    # print("输入测试特征值，获取预测结果：", predict)

    # 非标准化：0.8947368421052632  多次运行出现不同正确率结果：   这是因为划分 训练集 与  测试集 时每次划分数据不一样导致
    # 标准化：0.9736842105263158
    # print("预测结果的准确率", knn.score(feature_test, target_test))

    accuracy = knn.score(feature_test, target_test)

    return accuracy


if __name__ == '__main__':
    acc_lsit = []
    for i in range(20):
        acc = iris_predicting()
        acc_lsit.append(acc)

    acc_df = pd.Series(acc_lsit)
    print(acc_df)

    x = acc_df.index
    y = acc_df.values

    plt.figure(figsize=(20, 8), dpi=60)

    plt.plot(x, y)

    plt.xticks(range(len(x)), x)
    plt.yticks([0.01*i for i in range(80, 100)][::2])

    plt.show()



