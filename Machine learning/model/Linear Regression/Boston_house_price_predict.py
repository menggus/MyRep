from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error


def sgd():

    data = load_boston()  # 获取数据

    x_train, x_test, y_train, y_test= train_test_split(data.data, data.target, test_size=0.25, random_state=24)  # 数据分割

    std_x = StandardScaler()  # 标准化实例
    std_y = StandardScaler()

    x_train = std_x.fit_transform(x_train)  # 标准化样本数据集
    x_test = std_x.transform(x_test)

    # #### 标准化过程中需要传入二维数组
    #     问题：ValueError: Expected 2D array, got 1D array instead  （版本升级）
    #     解决：y_train.reshape(-1,1)

    y_train = std_y.fit_transform(y_train.reshape(-1, 1))  # 标准化目标集
    y_test = std_y.transform(y_test.reshape(-1, 1))

    # #### 构造线性回归模型
    #     正规方程
    #     梯度下降

    # lr = LinearRegression()
    lr = SGDRegressor()
    lr.fit(x_train, y_train)

    print("权重值：", lr.coef_)  # 线性回归 权重 w 的值

    predict_price = std_y.inverse_transform(lr.predict(x_test))  # 预测房价数据

    print("均方误差：", mean_squared_error(std_y.inverse_transform(y_test), predict_price))

