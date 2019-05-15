import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier


def randomforest():
    # #### 获取数据

    data = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")  # data : DataFrame

    x = data[["pclass", "age", "sex"]]  # 特征选择
    y = data["survived"]  # 目标值选择

    x["age"].fillna(x["age"].mean(), inplace=True)  # 使用平均值填充缺失值

    # #### 特征抽取

    dv = DictVectorizer(sparse=False)
    x = dv.fit_transform(x.to_dict(orient="records"))  # records : list like [{column -> value}, … , {column -> value}]

    # #### 分割数据集

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=25)

    # #### 模型

    rf = RandomForestClassifier()

    # #### 超参数（参数调优）
    # #### n_estimators = [120, 200, 300, 500, 800, 1200]
    # #### max_depth= [5, 8, 15, 25, 30]

    param = {"n_estimators": [50, 100, 120, 200, 500], "max_depth": [5, 8, 15, 25, 30]}
    gc = GridSearchCV(rf, param_grid=param, cv=2)
    gc.fit(x_train, y_train)

    gc.score(x_test, y_test)  # 准确率

    print("best_estimator：", gc.best_estimator_)  # 最好的估计器

    print("best_params:", gc.best_params_)  # 最好的参数

    print("best_score:", gc.best_score_)  # 交叉验证中最好的准确率得分

    print("best_index:", gc.best_index_)


