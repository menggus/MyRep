# coding: utf-8
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report


def logisticR():
    # 获取数据

    # 数据中无列名， 所以需要设置
    column = ['Sample code number','Clump Thickness', 'Uniformity of Cell Size','Uniformity of Cell Shape',
              'Marginal Adhesion', 'Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class']


    data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data",
                       header=None,
                       names=column
                       )

    data = data.replace("?", np.nan)  # 替换数据中的 ？ 号
    data = data.dropna()

    # #### 分割数据集   标准化处理

    x_train, x_test, y_train, y_test = train_test_split(data.iloc[:,1:10], data.iloc[:,10], test_size=0.25)

    # 标准化
    std = StandardScaler()
    x_train = std.fit_transform(x_train.astype("float"))
    x_test = std.transform(x_test.astype("float"))

    # #### 模型
    lg = LogisticRegression(C=1.0)
    lg.fit(x_train, y_train)
    predict_res = lg.predict(x_test)

    # 准确率
    print("预测准确率:", lg.score(x_test, y_test))

    # 分类文本报告
    report = classification_report(y_test, predict_res, labels=[2, 4], target_names=["良性", "恶性"])

    print(report)


if __name__ == '__main__':
    logisticR()