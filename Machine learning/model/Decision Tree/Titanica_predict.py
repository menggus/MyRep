import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import pydotplus
from IPython.display import Image


def decisiontree():
    # #### 获取数据

    data = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")  # data : DataFrame

    x = data[["pclass", "age", "sex"]]  # 特征选择

    y = data["survived"]  # 目标值选择

    # #### 缺失值处理

    x["age"].fillna(x["age"].mean(), inplace=True)  # 使用平均值填充缺失值

    # #### 特征抽取

    dv = DictVectorizer(sparse=False)

    x = dv.fit_transform(x.to_dict(orient="records"))  # records : list like [{column -> value}, … , {column -> value}]

    # #### 分割数据集

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # #### 进行模型训练

    dv.get_feature_names()  # 特征值名称

    dtree = DecisionTreeClassifier()

    dtree.fit(x_train, y_train)

    predict_res = dtree.predict(x_test)  # 进行预测，得出预测结果

    print("预测结果:", predict_res)

    print("准确率:", dtree.score(x_test, y_test))

    # ####  树的可视化

    dot_data = export_graphviz(
        dtree, # 树模型
        out_file=None, # 导出文件
        feature_names=dv.get_feature_names(),  # 特征值，分类依据
        filled=True,
        impurity=False,
        rounded=True
    )

    graph = pydotplus.graph_from_dot_data(dot_data)
    graph.get_nodes()[7].set_fillcolor("#FFF2DD")

    Image(graph.create_png())

