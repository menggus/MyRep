import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


def knn_predict():
    """
        facebook_v_predict : skaggle competition
    :return:
    """
    # 读取本地
    data = pd.read_csv(r"C:\Users\tao_cp\Music\kaggle\facebook-v-predicting-check-ins\train.csv")  # 读取本地文件
    # 数据预处理
    # 1.缩小数据集：DataFrame.query()对data进行数据缩小 “条件”
    # 2.时间序列化：对data中列 time 进行时间序列化，利于时间特征的使用，提取月、天、日
    # 3.分组操作：统计place_id使用次数，删除次数小于3的数据
    data.query("x > 1.0 &  x < 2.0 & y > 1 & y < 2", inplace=True)
    time_data = pd.DatetimeIndex(data["time"])

    data["weekday"] = time_data.weekday
    data["day"] = time_data.day
    data["hour"] = time_data.hour
    data = data.drop("time", axis=1)
    data_group = data.groupby(by="place_id").count()
    # reset_index(): 重置索引，旧索引变为列名为"place_id"的列
    data_re = data_group[data_group.row_id > 3].reset_index()

    # 获取模型数据集
    data = data[data["place_id"].isin(data_re.place_id)]
    y = data["place_id"]  # 获取目标值

    x = data.drop("place_id", axis=1)  # 获取特征值,
    x = x.drop("row_id", axis=1)  # 删除row_id提取有用特征

    # # 分割数据集
    feature_train, feature_test, target_train, target_test = train_test_split(x, y, test_size=0.25)

    # 特征值的标准化
    std = StandardScaler()
    feature_train = feature_train.astype("float")
    feature_test = feature_test.astype("float")

    feature_train =std.fit_transform(feature_train)
    feature_test = std.transform(feature_test)

    # 模型选择
    knn = KNeighborsClassifier()


    # 网格搜索
    param = {"n_neighbors": [3, 5, 8]}
    gscv = GridSearchCV(knn, param_grid=param, cv=2)
    gscv.fit(feature_train, target_train)

    #预测
    res_predict = gscv.predict(feature_test)

    print("预测的正确率：", res_predict)
    print("交叉验证最好的情况:", gscv.best_score_)
    print("交叉验证最好的参数:", gscv.best_params_)
    print("最好模型：", gscv.best_estimator_)
    print("每次交叉验证的结果：", gscv.cv_results_)


if __name__ == '__main__':
    knn_predict()





