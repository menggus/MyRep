import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


# read data
file_path = "./911.csv"
data = pd.read_csv(file_path)
# print(data.info())
# print(data["title"].head())

# get data 给data拼接新的cate列，表示分类
# 方法一:
temp_list = data["title"].str.split(":")
data["Cate"] = [i[0] for i in temp_list]  # list也可以，ndarray，Series，DataFrame也可以，注意index
# 方法二：assign，assign新增列不支持list操作，官方文档示例都只支持字符串和数值型的操作
# data1 = data.assign(Cate=lambda x: x['title'].str.split(":")[0])

# 分组
data_cate = data["Cate"].groupby(by=data["Cate"]).count()

# 准备绘图数据
x = data_cate.index
y = data_cate.values

plt.figure(figsize=(20, 8), dpi=60)

plt.bar(x, y, width=0.5)

plt.show()








