import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
"""dataframe：时间序列的使用"""
"""绘制不同月份的电话次数"""


# read data
file_path = "./911.csv"
data = pd.read_csv(file_path)
# print(data.info())
# print(data["timeStamp"].head())

# 把timeStamp列转化为DataFrame中的时间序列
# data = data.set_index(data["timeStamp"])
data["timeStamp"] = pd.to_datetime(data["timeStamp"])
data.set_index("timeStamp", inplace=True)

diff_month_data = data["title"].resample("M").count()

# 准备绘图数据
x = diff_month_data.index
y = diff_month_data.values


plt.figure(figsize=(20, 8), dpi=60)

plt.plot(x, y)

plt.xticks(x, x.strftime("%Y-%m-%d"), rotation=45)

plt.show()


